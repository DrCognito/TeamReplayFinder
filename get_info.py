from argparse import ArgumentParser
from os import environ as environment

from dotenv import load_dotenv
from pandas import DataFrame, read_sql, concat
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

from replay_finder.model import InitDB, League, LeagueStatus, Replay


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


def get_league_info(league_id: int, session):
    sql_statement = session.query(League).filter(League.league_id == league_id)
    data = read_sql(sql_statement.statement, session.bind)

    replay_count = session.query(Replay).filter(Replay.league_id == league_id).count()
    data['Count'] = replay_count

    return data


def get_team_info(league_id: int, session):
    pass


def get_player_info(player_id: int, session):
    pass


if __name__ == '__main__':
    args = arguments.parse_args()
    engine = InitDB(environment['REPLAY_LEAGUE_DB_PATH'])
    Session = sessionmaker(bind=engine)
    session = Session()

    if args.league_ids is not None:
        league_info = map(lambda x: get_league_info(x, session),
                          args.league_ids)

        league_df = concat(league_info)
        if args.csv_output:
            print(league_df.to_csv())
        else:
            print(tabulate(league_df, headers='keys'))

    if args.team_ids is not None:
        team_info = map(lambda x: get_team_info(x, session),
                        args.team_ids)

    if args.player_id is not None:
        player_info: DataFrame = get_player_info(args.player_id, session)