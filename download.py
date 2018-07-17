from argparse import ArgumentParser
from datetime import datetime, timedelta
from os import environ as environment

from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from replay_finder.model import InitDB as replay_InitDB
from replay_finder.model import Replay, get_replays_for_team
from replay_finder.team_info import InitTeamDB, TeamInfo

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
                       help="""Set a custom time for replays""")


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

    replay_query = get_replays_for_team(team, replay_session)
    print("Found {} replays".format(replay_query.count()))