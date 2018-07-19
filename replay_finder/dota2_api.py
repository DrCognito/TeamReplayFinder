from os import environ as environment

from dota2.util import replay_url_from_match
from steam.enums import EResult

from replay_finder import dota2_client, steam_client


def gc_login():
    user = environment['STEAM_USER']
    password = environment['STEAM_PASS']

    status = steam_client.cli_login(user, password)

    if status != EResult.OK:
        print('Login failed returning: ', status)


class SingleDotaClient(object):
    __instance = None

    def __new__(cls, token):
        if SingleDotaClient.__instance is None:
            SingleDotaClient.__instance = object.__new__(cls)

            SingleDotaClient.__instance.token = token
            SingleDotaClient.__instance.dota2_client = dota2_client
            SingleDotaClient.__instance.steam_client = steam_client
            SingleDotaClient.__instance.dota2_ready = False
            gc_login()

        return SingleDotaClient.__instance

    @steam_client.on('logged_on')
    def __start_dota():
        print('Launching dota 2 game controller.')
        SingleDotaClient.__instance.dota2_client.launch()
        SingleDotaClient.__instance.dota2_client.emit('dota2_ready')
        SingleDotaClient.__instance.steam_client.wait_event('finished')

    @dota2_client.on('ready')
    def __dota_ready():
        SingleDotaClient.__instance.dota2_ready = True

    @dota2_client.on("match_details")
    def emit_replay_id(replay_id, eresult, replay):
        url = replay_url_from_match(replay)
        print(url)
        SingleDotaClient.__instance.dota2_client.emit("replay_url", replay_id, url)

    def close(cls):
        SingleDotaClient.__instance.steam_client.emit('finished')
        SingleDotaClient.__instance.dota2_ready = False
        SingleDotaClient.__instance.dota2_client.exit()
        SingleDotaClient.__instance.steam_client.disconnect()

    def dota_wait(cls, *args, **kwargs):
        return SingleDotaClient.__instance.dota2_client\
                               .wait_event(*args, **kwargs)

    def steam_wait(cls, *args, **kwargs):
        return SingleDotaClient.__instance.steam_client\
                               .wait_event(*args, **kwargs)
