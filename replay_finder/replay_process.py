from bz2 import BZ2File
from os import remove as remove_file, environ
from time import sleep

import d2api
from requests import get as req_get, Session as requests_Session
from requests import codes as req_codes
from requests.exceptions import (ConnectionError, HTTPError, InvalidURL,
                                 RequestException)
from sqlalchemy.exc import SQLAlchemyError
from tqdm import tqdm
from pathlib import Path

from .__init__ import GC_API_LIMIT, WEB_API_LIMIT, REPLAY_DOWNLOAD_DELAY, REPLAY_DOWNLOAD_GIVEUP
from .api_usage import APIOverLimit, DecoratorUsageCheck
from .model import ReplayStatus, Replay,get_gc_usage, get_api_usage, make_replay
from .match_draft import save_match_draft

from datetime import datetime


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
        remove_file(path_out)
        #raise FileExistsError
    if not path_in.is_file():
        print("{} replay bz2 file does not exist".format(path_in))
        raise FileNotFoundError

    failed_file = False
    with open(path_out, 'wb') as out_file, BZ2File(path_in, mode="rb") as file:
        try:
            for data in iter(lambda: file.read(100 * 1024), b''):
                out_file.write(data)
        except OSError:
            print('Failed to extract {}.'.format(path_in))
            failed_file = True

    if remove_archive:
        remove_file(path_in)

    if failed_file:
        if path_out.is_file():
                remove_file(path_out)
        return False

    return path_out


def replay_process_odota(replay: Replay, session, req_session):
    def _query_odota(replay_id):
        base_url = 'https://api.opendota.com/api/matches/{}'.format(replay_id)
        responce = req_session.get(base_url, timeout=10)

        if responce.status_code != req_codes.ok:
            print("Failed to retrieve {} from odota with code {}"
                  .format(base_url, responce.status_code))
        try:
            json = responce.json()
            return json['replay_url']
        except (ValueError, KeyError):
            print("Invalid json retrieved from {}"
                  .format(base_url))
            return None

    if replay.status == ReplayStatus.DOWNLOADED:
        return False

    extract_path = Path(environ["EXTRACT_PATH"]) /\
            (str(replay.replay_id) + '.dem')

    if extract_path.is_file():
        print("Found {} in extract path skipping.".format(replay.replay_id))
        replay.status = ReplayStatus.DOWNLOADED
        session.merge(replay)
        session.commit()
        return extract_path

    if replay.status == ReplayStatus.ACKNOWLEDGED:
        if replay.process_attempts > GC_REPLAY_ATTEMPTS:
            print("Attempts exceeded for {}. Skipping."
                  .format(replay.replay_id))
            return False

        url = _query_odota(replay.replay_id)
        replay.process_attempts += 1
        session.merge(replay)
        session.commit()
        sleep(3)

        if url is None:
            raise ValueError
            # return replay_process_odota(replay, session, req_session)

        replay.replay_url = url
        replay.status = ReplayStatus.DOWNLOADING
        replay.process_attempts = 0
        session.merge(replay)
        session.commit()

        return replay_process_odota(replay, session, req_session)

    if replay.status == ReplayStatus.DOWNLOADING:
        # if replay.process_attempts > REPLAY_DOWNLOAD_ATTEMPTS:
        #     print("Download attempts exceeded for {}. Skipping."
        #           .format(replay.replay_id))
        #     return False
        if replay.last_download_time is None:
            replay.last_download_time = datetime.now()
            session.merge(replay)
            session.commit()
        elif datetime.now() - replay.last_download_time < REPLAY_DOWNLOAD_DELAY:
            print(f"Skipping {replay.replay_id} was tried {datetime.now() - replay.last_download_time} ago.")
            return False
        elif (datetime.now() - replay.start_time) > REPLAY_DOWNLOAD_GIVEUP and replay.process_attempts > 1:
            print(f"Skipping {replay.replay_id}. Has not been found after {REPLAY_DOWNLOAD_GIVEUP} and {replay.process_attempts}")
            replay.status = ReplayStatus.FAILED
            session.merge(replay)
            session.commit()
            return False

        download_path = Path(environ["DOWNLOAD_PATH"]) /\
            (str(replay.replay_id) + '.dem.bz2')
        try:
            download_replay(replay, download_path)
        except RequestException as e:
            print(e)
            sleep(5)
            return replay_process_odota(replay, session, req_session)
        finally:
            replay.last_download_time = datetime.now()
            replay.process_attempts += 1
            session.merge(replay)
            session.commit()
            sleep(1)

        final_path = extract_replay(download_path, extract_path)
        if final_path:
            replay.status = ReplayStatus.DOWNLOADED
        session.merge(replay)
        session.commit()

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


def add_single_replay(session, match_id: int):
    dota2_webapi = d2api.APIWrapper()

    @DecoratorUsageCheck(session, get_api_usage, WEB_API_LIMIT)
    def _get_replay_details(web_query):
        return dota2_webapi.get_match_details(**web_query)

    try:
        match_query = _get_replay_details({'match_id': match_id})
    except (d2api.errors.APITimeoutError, d2api.errors.BaseError) as e:
        print(f"Failed to add {match_id}, valve Dota2 API Time Out.")
        return
    sleep(1)

    new_replay = make_replay(match_query)
    save_match_draft(match_query)
    try:
        session.add(new_replay)
        session.commit()
    except SQLAlchemyError as e:
        print("Failed to add new match {}".format(match_id))
        print(e)
        session.rollback()

    return new_replay.start_time
