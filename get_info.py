from argparse import ArgumentParser
from os import environ as environment

from dotenv import load_dotenv
from pandas import DataFrame, read_sql, concat
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

from replay_finder.model import InitDB, League, Replay
from replay_finder.team_info import InitTeamDB, TeamInfo, TeamPlayer


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


def get_team_replays(team_id: int, session, team_session):
    team: TeamInfo = team_session.query(TeamInfo)\
                                 .filter(TeamInfo.team_id == team_id).one()
    team_stack = team.stack_id

    dire_statement = team_session.query(Replay)\
                                 .filter((Replay.dire_id == team_id) |
                                         (Replay.dire_stack_id == team_stack))
    data_dire = read_sql(dire_statement.statement, session.bind)

    radiant_statement = team_session.query(Replay)\
                                    .filter((Replay.radiant_id == team_id) |
                                            (Replay.radiant_stack_id == team_stack))
    data_radiant = read_sql(radiant_statement.statement, session.bind)


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

    if args.player_id is not None:
        player_info: DataFrame = get_player_info(args.player_id, session)

        if args.csv_output:
            print(player_info.to_csv())
        else:
            print(tabulate(player_info, headers='keys'))