import gevent.monkey
gevent.monkey.patch_all()
from argparse import ArgumentParser
from time import sleep
from os import environ as environment

from dota2api import convert_to_64_bit
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


def get_team_info(team_id: int, req_session):
    "Attempts to retrieve from ODOTA the name and players"
    "using the provided team_id, returned in that order."
    base_url = 'https://api.opendota.com/api/teams/{}'.format(team_id)
    base_url_players = base_url + '/players'

    def _query_odota(url):
        print(url)
        responce = req_session.get(url)
        #responce = req_get(url)
        print("boo")
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

    for p in players:
        try:
            if p['is_current_team_member']:
                pid = convert_to_64_bit(p['account_id'])
                name = p['name']
                out_string += "PlayerIDs['{}']"\
                                 "['{}'] = {}\n".format(team_name, name, pid)
        except KeyError:
            print("Failed to process team {}".format(team_id))
            return None

    out_string += "ValidityTime['{}'] = "\
                  "datetime.datetime(2018, 9, 14, 0, 0, 0, 0)\n".format(team_name)
    out_string += "_TeamIDs['{}'] = {}\n".format(team_name, team_id)

    return out_string

if __name__ == '__main__':
    args = arguments.parse_args()

    with requests_Session() as req_session:
        for t in args.team_ids:
            print(t)
            print(get_team_info(t, req_session))

