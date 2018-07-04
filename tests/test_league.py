import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import sessionmaker

from replay_finder.model import InitDB
from replay_finder.league import update_league_listing, update_league_replays

engine = InitDB('sqlite://')
Session = sessionmaker(bind=engine)
session = Session()

# International 2018 qualifier
test_id = 10049

update_league_listing(session)