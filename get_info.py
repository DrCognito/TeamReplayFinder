from argparse import ArgumentParser
from os import environ as environment

from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker


load_dotenv(dotenv_path="setup.env")

arguments = ArgumentParser
arguments.add_argument('--league_ids',
                       help=r"Display known information about league_id",
                       nargs="*",
                       type=int)
arguments.add_argument('--team_ids',
                       help="""Display known information about team_id
                               by numerical ID""",
                       nargs="*",
                       type=int)
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


def get_league_info(league_id: int):
    pass


def get_team_info(league_id: int):
    pass


def get_player_info(player_id: int):
    pass


if __name__ == '__main__':
    args = arguments.parse_args()

    if args.league_ids is not None:
        league_info = map(get_league_info, args.league_ids)

    if args.team_ids is not None:
        team_info = map(get_team_info, args.team_ids)

    if args.player_id is not None:
        player_info = get_player_info(args.player_id)