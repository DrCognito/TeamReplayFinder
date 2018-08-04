from argparse import ArgumentParser
from datetime import datetime, timedelta
from os import environ as environment
from pathlib import Path

from gevent import Timeout as GeventTimeout
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from replay_finder.dota2_api import SingleDotaClient
from replay_finder.model import InitDB as replay_InitDB
from replay_finder.model import Replay, ReplayStatus, get_replays_for_team
from replay_finder.replay_process import check_existance, replay_process_odota
from replay_finder.team_info import InitTeamDB, TeamInfo
import requests

REPLAY_TIME_PERIOD_DAYS = 30

arguments = ArgumentParser()
arguments.add_argument('team', help="""Team name or team id from
                                       the TeamInfo database.""")
arguments.add_argument('--list',
                       help="""Only list replays.
                               Skips updating or
                               downloading replays.""",
                       action='store_true')
arguments.add_argument('--custom_time',
                       help="""Set a custom time for replays""",
                       type=int)
arguments.add_argument('--require_players',
                       help="""Require both the team id and player
                               stack to match.""",
                       action='store_true')
arguments.add_argument('--limit',
                       help='''Limit number of replays to download.''',
                       type=int
                       )

replay_paths = [
    Path(environment['JSON_ARCHIVE']),
    Path(environment['JSON_PATH']),
    Path(environment['EXTRACT_PATH']),
    Path(environment['DOWNLOAD_PATH'])
]
replay_extensions = [
    '.json',
    '.json',
    '.dem',
    '.dem.bz2',
]


if __name__ == '__main__':
    args = arguments.parse_args()
    updatecut = timedelta(days=REPLAY_TIME_PERIOD_DAYS)

    if args.custom_time is not None:
        updatecut = timedelta(days=args.custom_time)

    replay_engine = replay_InitDB(environment['REPLAY_LEAGUE_DB_PATH'])
    replay_Session = sessionmaker(bind=replay_engine)
    replay_session = replay_Session()

    team_engine = InitTeamDB(environment['TEAM_DB_PATH'])
    team_Session = sessionmaker(bind=team_engine)
    team_session = team_Session()

    t_filter = or_(TeamInfo.team_id == args.team,
                   TeamInfo.name == args.team)
    team = team_session.query(TeamInfo).filter(t_filter).one_or_none()

    if team is None:
        print("Could not find team corresponding to {}"
              .format(args.team))
        exit()

    if args.require_players:
        replays = get_replays_for_team(team, replay_session, require_both=True)
    else:
        replays = get_replays_for_team(team, replay_session,
                                       require_both=False)
    replays = replays.filter(Replay.start_time > datetime.now() - updatecut)\
                     .order_by(Replay.replay_id.desc())

    if args.list:
        output = "Total:\t" + str(replays.count()) + "\n"
        output += "Replay\t\tStatus\t\tPath\n"
        for rep in replays:
            output += str(rep.replay_id) + "\t"
            output += str(rep.status) + "\t"
            path = check_existance(rep, replay_extensions, replay_paths)
            output += str(path) + "\n"
        print(output)
        exit()

    # Start up the steam client!
    # dota_client = SingleDotaClient("download")
    # try:
    #     dota_client.dota_wait('ready', timeout=20, raises=True)
    # except GeventTimeout:
    #     print("Timed out waiting for dota2 client to ready.")
    #     dota_client.close()
    #     exit()

    replays = replays.filter(Replay.status != ReplayStatus.DOWNLOADED,
                             Replay.status != ReplayStatus.FAILED)
    if args.limit is not None:
        replays = replays.limit(args.limit)

    with requests.Session() as req_session:
        for rep in replays:
            path = replay_process_odota(rep, replay_session, req_session)
            if path:
                print("Replay downloaded to: {}".format(path))
            else:
                print("Failed to process replay {}.".format(rep.replay_id))
