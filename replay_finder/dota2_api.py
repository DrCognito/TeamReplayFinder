from __init__ import dota2_client, steam_client
from dota2.util import replay_url_from_match
from steam.enums import EResult
import os


# Setup
@steam_client.on('logged_on')
def start_dota():
    print("Launching dota 2 gc.")
    dota2_client.launch()


def gc_login():
    user = os.environ['STEAM_USER']
    password = os.environ['STEAM_PASS']

    status = steam_client.cli_login(user, password)

    if status != EResult.OK:
        print('Login failed returning: ', status)