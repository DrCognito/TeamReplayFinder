from argparse import ArgumentParser
from os import environ as environment

from dotenv import load_dotenv
from pandas import DataFrame, read_sql, concat
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from pathlib import Path

from download import replay_paths, replay_extensions
from TeamReplayFinder.replay_finder.model import InitDB, League, Replay
from TeamReplayFinder.replay_finder.team_info import InitTeamDB, TeamInfo, TeamPlayer


load_dotenv(dotenv_path="setup.env")

arguments = ArgumentParser()
arguments.add_argument('--league_ids',
                       help="Display known information about league_id",
                       nargs="*",
                       type=int
                       )
arguments.add_argument('--team_ids',
                       help="""Display known information about team_id
                               by numerical ID""",
                       nargs="*",
                       type=int
                       )
arguments.add_argument('--teams',
                       help="""Display known information about team
                               by name""",
                       nargs="*")
arguments.add_argument('--replays',
                       help="Lookup information on replays and check"
                            "available locations for the id.",
                       type=int,
                       nargs="*")
arguments.add_argument('--player_id',
                       help="""Display known information about player
                               by steam ID""",
                       type=int)
arguments.add_argument('--csv_output',
                       help="""Output using pandas DataFrame to_csv""",
                       action='store_true')
arguments.add_argument('--list_replays',
                       help="""List replays for requested team_ids""",
                       action='store_true')
arguments.add_argument('--max_replays',
                       help="Maximum number of replays to list.",
                       type=int,
                       default=30)
arguments.add_argument('--generate_id',
                       help="Generate a stack_id from a" 
                       "list of 5 player ids",
                       nargs="*",
                       type=int)


def get_league_info(league_id: int, session):
    sql_statement = session.query(League).filter(League.league_id == league_id)
    data = read_sql(sql_statement.statement, session.bind)

    replay_count = session.query(Replay).filter(Replay.league_id == league_id).count()
    data['Count'] = replay_count

    return data


def get_team_info(team_id: int, team_session):
    sql_statement = team_session.query(TeamInfo).filter(TeamInfo.team_id == team_id)
    data = read_sql(sql_statement.statement, team_session.bind)

    return data


def get_teamplayer_info(team_id: int, team_session):
    sql_statement = team_session.query(TeamPlayer).filter(TeamPlayer.team_id == team_id)
    data = read_sql(sql_statement.statement, team_session.bind)

    return data


def get_player_info(player_id: int, team_session):
    sql_statement = team_session.query(TeamPlayer).filter(TeamPlayer.player_id == player_id)
    data = read_sql(sql_statement.statement, team_session.bind)

    return data


def get_team_replays(team_id: int, session, team_session, max_count=50):
    team: TeamInfo = team_session.query(TeamInfo)\
                                 .filter(TeamInfo.team_id == team_id).one()
    team_stack = team.stack_id

    dire_statement = team_session.query(Replay.replay_id.label('Dire'))\
                                 .filter((Replay.dire_id == team_id) |
                                         (Replay.dire_stack_id == team_stack))\
                                 .order_by(Replay.replay_id.desc())\
                                 .limit(max_count)
    data_dire = read_sql(dire_statement.statement, session.bind)

    radiant_statement = team_session.query(Replay.replay_id.label('Radiant'))\
                                    .filter((Replay.radiant_id == team_id) |
                                            (Replay.radiant_stack_id ==
                                             team_stack))\
                                    .order_by(Replay.replay_id.desc())\
                                    .limit(max_count)
    data_radiant = read_sql(radiant_statement.statement, session.bind)

    return data_dire, data_radiant


def get_replay_db_info(replay_id: int, session):
    sql_statement = session.query(Replay.replay_id, Replay.start_time,
                                  Replay.league_id, Replay.status,
                                  Replay.dire_id, Replay.radiant_id)\
                           .filter(Replay.replay_id == replay_id)
    data = read_sql(sql_statement.statement, session.bind)

    return data


def get_replay_location_info(replay_id: int):
    data = DataFrame()
    for f_path, ext in zip(replay_paths, replay_extensions):
        r_file: Path = f_path / (str(replay_id) + ext)
        column = "{}\\*{}".format(str(f_path), ext)
        data[column] = [r_file.is_file(), ]
    data.index = [replay_id, ]

    return data


def generate_stack_id(id_list: list):
    assert(len(id_list) == 5)
    assert(len(set(id_list)) == len(id_list))
    id_list.sort()

    return ''.join(str(p) for p in id_list)

if __name__ == '__main__':
    args = arguments.parse_args()

    engine = InitDB(environment['REPLAY_LEAGUE_DB_PATH'])
    Session = sessionmaker(bind=engine)
    session = Session()

    team_engine = InitTeamDB(environment['TEAM_DB_PATH'])
    Team_Session = sessionmaker(bind=team_engine)
    team_session = Team_Session()

    if args.league_ids is not None:
        league_info = map(lambda x: get_league_info(x, session),
                          args.league_ids)

        league_df = concat(league_info)
        if args.csv_output:
            print(league_df.to_csv())
        else:
            print(tabulate(league_df, headers='keys'))

    if args.team_ids is not None:
        team_info = map(lambda x: get_team_info(x, team_session),
                        args.team_ids)
        team_df = concat(team_info)

        if args.csv_output:
            print(team_df.to_csv())
        else:
            print(tabulate(team_df, headers='keys'))

        if args.list_replays:
            teams_replays = map(lambda x: get_team_replays(x, session,
                                team_session, max_count=args.max_replays),
                                args.team_ids)

            for r in teams_replays:
                summary = concat(r, axis=1)
                if args.csv_output:
                    print(summary.to_csv())
                else:
                    print(tabulate(summary, headers='keys', floatfmt='.0f'))

    if args.replays is not None:
        replay_itter = map(lambda x: get_replay_db_info(x, session),
                           args.replays)
        replay_info = concat(replay_itter)

        replay_itter = map(lambda x: get_replay_location_info(x),
                           args.replays)
        replay_locations = concat(replay_itter)

        if args.csv_output:
            print(replay_info.to_csv())
            print(replay_locations.to_csv())
        else:
            print(tabulate(replay_info, headers='keys'))
            print(tabulate(replay_locations, headers='keys'))
            #print(replay_locations)

    if args.player_id is not None:
        player_info: DataFrame = get_player_info(args.player_id, team_session)
        player_info.index = player_info["player_id"]

        if args.csv_output:
            print(player_info.to_csv())
        else:
            print(tabulate(player_info, headers='keys'))

    if args.generate_id is not None:
        print("Generating stack id for {}".format(str(args.generate_id)))
        print(generate_stack_id(args.generate_id))