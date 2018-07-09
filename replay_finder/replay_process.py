from requests import get as req_get
from requests.exceptions import InvalidURL, ConnectionError, RequestException
from requests.exceptions import HTTPError
from tqdm import tqdm
from bz2 import BZ2File


def download_replay(replay, path):
    if path.is_file():
        print("{} already exists.".format(path))
        raise FileExistsError
    if replay.replay_url is None:
        print("Url in replay is none.")
        raise InvalidURL

    print("Downloading: {}".format(replay.replay_url))
    try:
        dl_stream = req_get(replay.replay_url)
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
            return False

    return True
