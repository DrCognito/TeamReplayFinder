from bz2 import BZ2File
from os import remove as remove_file, environ
from time import sleep

# from dota2.util import replay_url_from_match
from requests import get as req_get
from requests.exceptions import (ConnectionError, HTTPError, InvalidURL,
                                 RequestException)
from tqdm import tqdm
from pathlib import Path

from .__init__ import GC_API_LIMIT
from .api_usage import APIOverLimit, DecoratorUsageCheck
from .model import ReplayStatus, get_gc_usage
from .dota2_api import SingleDotaClient

from gevent import Timeout as GeventTimeout

GC_REPLAY_ATTEMPTS = 5
REPLAY_DOWNLOAD_ATTEMPTS = 3


def download_replay(replay, path):
    if path.is_file():
        print("{} already exists.".format(path))
        raise FileExistsError
    if replay.replay_url is None:
        print("Url in replay is none.")
        raise InvalidURL

    print("Downloading: {}".format(replay.replay_url))
    try:
        dl_stream = req_get(replay.replay_url, stream=True)
    except ConnectionError:
        print("Connection error!")
        return
    except HTTPError:
        print("Starting connection to {} failed with {}."
              .format(replay.replay_url, dl_stream.status_code))
        return

    with open(path, 'wb') as file:
        for data in tqdm(dl_stream.iter_content(chunk_size=10000)):
            file.write(data)

    return path


def extract_replay(path_in, path_out, remove_archive=True):
    if path_out.is_file():
        print("{} already exists.".format(path_out))
        raise FileExistsError
    if not path_in.is_file():
        print("{} replay bz2 file does not exist".format(path_in))
        raise FileNotFoundError

    with open(path_out, 'wb') as out_file, BZ2File(path_in, mode="rb") as file:
        try:
            for data in iter(lambda: file.read(100 * 1024), b''):
                out_file.write(data)
        except OSError:
            print('Failed to extract {}.'.format(path_in))
            if path_out.is_file():
                remove_file(path_out)
            return False

    if remove_archive:
        remove_file(path_in)

    return path_out


def process_replay(replay, session, dota_singleton: SingleDotaClient):
    @DecoratorUsageCheck(session, get_gc_usage, GC_API_LIMIT)
    def _replay_details(replay_id):
        dota_singleton.dota2_client.request_match_details(replay_id)

    if replay.status == ReplayStatus.DOWNLOADED:
        return False

    if replay.status == ReplayStatus.ACKNOWLEDGED:
        if replay.process_attempts > GC_REPLAY_ATTEMPTS:
            print("Attempts exceeded for {}. Skipping."
                  .format(replay.replay_id))
            return False

        try:
            _replay_details(replay.replay_id)
        except APIOverLimit as e:
            print(e)
            return False
        else:
            replay.process_attempts += 1
            session.merge(replay)
            session.commit()
        finally:
            sleep(1)

        try:
            rep_id, url = dota_singleton.dota_wait("replay_url", timeout=5,
                                                   raises=True)
        except GeventTimeout:
            print("Timed out retrieving replay url {}".format(replay.replay_id))
            url = None

        if url is None:
            raise TimeoutError
            return process_replay(replay, session, dota_singleton)

        replay.replay_url = url
        replay.status = ReplayStatus.DOWNLOADING
        replay.process_attempts = 0
        session.merge(replay)
        session.commit()

        return process_replay(replay, session, dota_singleton)

    if replay.status == ReplayStatus.DOWNLOADING:
        if replay.process_attempts > REPLAY_DOWNLOAD_ATTEMPTS:
            print("Download attempts exceeded for {}. Skipping."
                  .format(replay.replay_id))
            return False

        download_path = Path(environ["DOWNLOAD_PATH"]) /\
            (str(replay.replay_id) + '.dem.bz2')
        try:
            download_replay(replay, download_path)
        except RequestException as e:
            print(e)
            sleep(5)
            return process_replay(replay, session, dota_singleton)
        finally:
            replay.process_attempts += 1
            session.merge(replay)
            session.commit()
            sleep(1)

        replay.status = ReplayStatus.DOWNLOADED
        session.merge(replay)
        session.commit()

        extract_path = Path(environ["EXTRACT_PATH"]) /\
            (str(replay.replay_id) + '.dem')
        final_path = extract_replay(download_path, extract_path)

        return final_path


def check_existance(replay, extensions, paths):
    ''' Check for replay existance in the list of paths.
        extensions is a list corresponding to the file exention
        for that path.
    '''
    for p, ext in zip(paths, extensions):
        r_file = p / (str(replay.replay_id) + ext)
        if r_file.is_file():
            return r_file

    return False
