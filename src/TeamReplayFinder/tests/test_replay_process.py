import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from replay_finder import dota2_client, dota2_ready, steam_client
from replay_finder.dota2_api import SingleDotaClient
from steam.enums import EResult
from dota2.util import replay_url_from_match
#import logging
from time import sleep
from gevent import Timeout
#logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)

test = SingleDotaClient('token')
@test.dota2_client.on("match_details")
def emit_replay_id(replay_id, eresult, replay):
    url = replay_url_from_match(replay)
    print(url)
    dota2_client.emit("replay_url", replay_id, url)


if not test.dota2_ready:
    print("waiting for dota2!")
    try:
        test.dota_wait('ready', timeout=30, raises=True)
    except Timeout:
        print("did not retrieve ready message.")
print('Requesting match')
test.dota2_client.request_match_details(3971673262)
test.dota2_client.wait_event('replay_url', timeout=30)
print('Closing')
test.close()
