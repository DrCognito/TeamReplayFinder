# import gevent.monkey
# gevent.monkey.patch_all()
# Steam GC api

from dotenv import load_dotenv
from datetime import timedelta

load_dotenv(dotenv_path="setup.env")

# dota2_webapi = Initialise()

WEB_API_LIMIT = 100000
# Unkown if it is this low, reported by dota2 docs.
GC_API_LIMIT = 100
# Datdota limit of 500 a day
# https://www.datdota.com/about
DATDOTA_API_LIMIT = 500

REPLAY_DOWNLOAD_DELAY = timedelta(minutes=5)
# The message on dotabuff says that replays missing for 3 hours rarely appear.
REPLAY_DOWNLOAD_GIVEUP = timedelta(hours=3)