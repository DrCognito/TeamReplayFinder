from pathlib import Path
from compression import zstd
file_in = Path("./8920668670_1743938090.dem.bz2")
file_out = Path("./8920668670.dem")

def extract_replay_zstd(path_in, path_out):
    # if path_out.is_file():
    #         print("{} already exists.".format(path_out))
    #         remove_file(path_out)
    #         #raise FileExistsError
    if not path_in.is_file():
        print("{} replay zstd file does not exist".format(path_in))
        raise FileNotFoundError
    
    failed_file = False
    with open(path_out, 'wb') as out_file, zstd.open(path_in) as file:
        file_content = file.read()
        try:
            out_file.write(file_content)
        except OSError as e:
            print(f'Extract error: {e}')
            print('Failed to extract {}.'.format(path_in))
            failed_file = True

    return failed_file