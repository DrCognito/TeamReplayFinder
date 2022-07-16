from argparse import ArgumentParser
from datetime import datetime, timedelta
from os import environ as environment
from pathlib import Path

from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from replay_finder.model import InitDB as replay_InitDB
from replay_finder.model import Replay, ReplayStatus, get_replays_for_team
from replay_finder.replay_process import check_existance, replay_process_odota
from replay_finder.team_info import InitTeamDB, TeamInfo
import requests

REPLAY_TIME_PERIOD_DAYS = 30

arguments = ArgumentParser()
arguments.add_argument('teams', help="""Team name or team id from
                                       the TeamInfo database.""",
                       nargs='+')
arguments.add_argument('--list',
                       help="""Only list replays.
                               Skips updating or
                               downloading replays.""",
                       action='store_true')
arguments.add_argument('--custom_time',
                       help="""Set a custom day age for replays""",
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

ImportantTimes = {
    'Patch_7_31': datetime(2022, 2, 23, 0, 0, 0, 0),
    'Stockholm2022': datetime(2022, 5, 12, 0, 0, 0, 0),
    'DPC2022_T3': datetime(2022, 6, 7, 0, 0, 0, 0),
    'RIYADH_2022': datetime(2022, 7, 20, 0, 0, 0, 0),
}


if __name__ == '__main__':
    args = arguments.parse_args()
    # updatecut = timedelta(days=REPLAY_TIME_PERIOD_DAYS)
    time_filter = Replay.start_time > ImportantTimes['DPC2022_T3']

    if args.custom_time is not None:
        updatecut = timedelta(days=args.custom_time)
        time_filter = Replay.start_time > datetime.now() - updatecut

    replay_engine = replay_InitDB(environment['REPLAY_LEAGUE_DB_PATH'])
    replay_Session = sessionmaker(bind=replay_engine)
    replay_session = replay_Session()

    team_engine = InitTeamDB(environment['TEAM_DB_PATH'])
    team_Session = sessionmaker(bind=team_engine)
    team_session = team_Session()

    failure_list = []
    for t_in in args.teams:
        t_filter = or_(TeamInfo.team_id == t_in,
                       TeamInfo.name == t_in)
        team = team_session.query(TeamInfo).filter(t_filter).one_or_none()

        if team is None:
            print("Could not find team corresponding to {}"
                  .format(t_in))
            exit()
        print(f"Processing {team.name}, {team.team_id}.")
        failure_list.append(f"Team {team.name}, {team.team_id}.\n")
        if args.require_players:
            replays = get_replays_for_team(team, replay_session, require_both=True)
        else:
            replays = get_replays_for_team(team, replay_session,
                                           require_both=False)
        replays = replays.filter(time_filter)\
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

        replays = replays.filter(Replay.status != ReplayStatus.DOWNLOADED,
                                 Replay.status != ReplayStatus.FAILED)
        if args.limit is not None:
            replays = replays.limit(args.limit)

        with requests.Session() as req_session:
            for rep in replays:
                try:
                    path = replay_process_odota(rep, replay_session, req_session)
                except TimeoutError:
                    print("TimeoutError for {}".format(rep.replay_id))
                    continue
                if path:
                    print("Replay downloaded to: {}".format(path))
                else:
                    print("Failed to process replay {}.".format(rep.replay_id))
                    failure_list.append(f"{rep.replay_id}\n")
    print(''.join(failure_list))
