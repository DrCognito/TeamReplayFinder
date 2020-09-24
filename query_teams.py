from base64 import urlsafe_b64encode
from datetime import datetime
from argparse import ArgumentParser
from time import sleep
from os import environ as environment

from util import convert_to_64_bit
from dotenv import load_dotenv
from requests import Session as requests_Session
from requests import codes as req_codes
from requests import get as req_get
from sqlalchemy.orm import sessionmaker

from replay_finder.team_info import InitTeamDB, build_team

load_dotenv(dotenv_path="setup.env")


arguments = ArgumentParser()
arguments.add_argument('team_ids',
                       help="Team ids to retrieve from ODOTA",
                       nargs='*')
arguments.add_argument('--print',
                       help="Print the team output instead of saving to file.",
                       action='store_true')
arguments.add_argument('--file',
                       help="Filename for team output.",
                       type=str)


def get_team_info(team_id: int, req_session):
    "Attempts to retrieve from ODOTA the name and players"
    "using the provided team_id, returned in that order."
    base_url = 'https://api.opendota.com/api/teams/{}'.format(team_id)
    base_url_players = base_url + '/players'

    def _query_odota(url):
        responce = req_session.get(url)
        sleep(2)

        if responce.status_code != req_codes.ok:
            print("Failed to retrieve team {} from odota with code {}"
                  .format(team_id, responce.status_code))
            print(url)
        try:
            return responce.json()
        except (ValueError, KeyError):
            print("Invalid json retrieved from {}"
                  .format(base_url))
            return None

    team = _query_odota(base_url)
    players = _query_odota(base_url_players)

    if team is None or players is None:
        print("Failed to process team {}".format(team_id))
        return None

    team_name = team['name']
    out_string = "PlayerIDs['{}'] = "\
                     "collections.OrderedDict()\n".format(team_name)

    player_strings = []
    for p in players:
        try:
            if p['is_current_team_member']:
                pid = convert_to_64_bit(p['account_id'])
                name = "".join(x for x in p['name'] if x.isalnum())
                p_string = "PlayerIDs['{}']"\
                           "['{}'] = {}\n".format(team_name, name, pid)
                player_strings.append(p_string)
        except KeyError:
            print("Failed to process team {}".format(team_id))
            return None

    while len(player_strings) < 5:
        player_strings.append("PlayerIDs['{}']"
                              "[''] = \n".format(team_name))

    for p in player_strings:
        out_string += p

    out_string += "ValidityTime['{}'] = "\
                  "datetime.datetime(2019, 9, 14, 0, 0, 0, 0)\n".format(team_name)
    out_string += "_TeamIDs['{}'] = {}\n".format(team_name, team_id)

    return out_string

if __name__ == '__main__':
    args = arguments.parse_args()

    output = str()
    now = datetime.now()
    output = "#Queried at {}\n".format(now.isoformat())
    with requests_Session() as req_session:
        for t in args.team_ids:
            print("Querying {}".format(t))
            output += get_team_info(t, req_session)
            output += "\n"
            #print(get_team_info(t, req_session))

    if len(args.team_ids) > 0:
        if args.print:
            print(output)
        else:
            if args.file is not None:
                file_name = args.file
            else:
                file_name = "team_template.py"
            with open(file_name, "w", encoding="utf-8") as file_out:
                file_out.write(output)

