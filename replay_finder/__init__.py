# import gevent.monkey
# gevent.monkey.patch_all()
# Steam GC api

from dotenv import load_dotenv

load_dotenv(dotenv_path="setup.env")

# dota2_webapi = Initialise()

WEB_API_LIMIT = 100000
# Unkown if it is this low, reported by dota2 docs.
GC_API_LIMIT = 100
# Datdota limit of 500 a day
# https://www.datdota.com/about
DATDOTA_API_LIMIT = 500
