import gevent.monkey
gevent.monkey.patch_all()
# Steam GC api
from steam import SteamClient
from dota2 import Dota2Client
# Web api
# from dota2api import Initialise

from dotenv import load_dotenv
from pathlib import Path
from json import load

load_dotenv(dotenv_path="setup.env")

# dota2_webapi = Initialise()

steam_client = SteamClient()
dota2_client = Dota2Client(steam_client)

# api_usage_path = Path('../data/api.json')
# if api_usage_path.is_file():
#     with open(api_usage_path, 'r') as file:
#         api_usage = load(file)

WEB_API_LIMIT = 100000
# Unkown if it is this low, reported by dota2 docs.
GC_API_LIMIT = 100
