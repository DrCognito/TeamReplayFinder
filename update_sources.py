import gevent.monkey
gevent.monkey.patch_all()
from argparse import ArgumentParser
from datetime import datetime, timedelta
from dotenv import load_dotenv
from os import environ as environment

from sqlalchemy.orm import sessionmaker

from replay_finder.league import update_league_listing, update_league_replays
from replay_finder.model import InitDB, League, LeagueStatus


load_dotenv(dotenv_path="setup.env")

UPDATE_TIME_PERIOD_DAYS = 0
UPDATE_TIME_PERIOD_HOURS = 22


arguments = ArgumentParser()
arguments.add_argument('--league_ids', help="""League IDs of the main leagues to be
                                            updated.
                                            Update will be forced even if it is
                                            less than the usual cut off time.
                                            """)
arguments.add_argument('--skip_league_update', help="""Skip updating the master league listing
                                                    """, action='store_true')
arguments.add_argument('--skip_replays', help="""Attempt to retrieve the basic information
                       for replays.""",
                       action='store_true')

if __name__ == '__main__':
    args = arguments.parse_args()
    updatecut = timedelta(days=UPDATE_TIME_PERIOD_DAYS,
                          hours=UPDATE_TIME_PERIOD_HOURS)
    
    extra_leagues = []
    if args.league_ids is not None:
        print("Forcing update for leagues: {}".format(args.league_ids))
        extra_leagues = args.league_ids
        
    engine = InitDB(environment['REPLAY_LEAGUE_DB_PATH'])
    Session = sessionmaker(bind=engine)
    session = Session()

    if not args.skip_league_update:
        update_league_listing(session)
        session.commit()

    if not args.skip_replays:
        league_ids = session.query(League.league_id)\
                    .filter(League.status != LeagueStatus.FINISHED)\
                    .filter(League.last_update < datetime.now() - updatecut)\
                    .order_by(League.league_id.desc())

        # sqlalchemy always returns a tuple for each row
        league_ids = [l[0] for l in league_ids.all()]
        league_ids = extra_leagues + league_ids

        for l in league_ids:
            print("Updating league {}".format(l))
            update_league_replays(session, l)
            session.commit()
