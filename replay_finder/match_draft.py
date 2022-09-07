# import d2api
# from d2api.src.wrappers import MatchDetails
# import requests
# import time
from dotenv import load_dotenv
from json import dump
from pathlib import Path
from os import environ as environment
from .HeroTools import heroByID

load_dotenv(dotenv_path="setup.env")
# api = d2api.APIWrapper()

# test_path = Path("./test.json")
# if not test_path.exists():
#     with open(test_path, "w") as f:
#         test_json = api.get_match_details(6701482389)
#         dump(test_json, f)
# else:
#     with open(test_path, "r") as f:
#         test_json = load(f)

# format = {"type": "PicksAndBans",
#           "cName": ["npc_dota...", "npc_dota...", "npc_dota..."],
#           "eName": ["CDOTA_Unit", "CDOTA_Unit", "CDOTA_Unit"],
#           "team": [2,3,2],
#           "ID": [25, 74, 38],
#           "isPick": [False, False, False],
#           "steamID": [76561198143985114,76561198053884305,76561198087883707],
#           "playerHero": ["npc_dota_hero_mars","npc_dota_hero_kunkka","npc_dota_hero_bloodseeker"],
#           "playerName":["AMMAR_THE_FUCKER","flight of the fireflies","Crystallis"],
#           "winningTeam":3,
#           "gameMode":2,
#           "matchID":6145307333,
#           "radiantTeamID":8261234,"direTeamID":1883502,
#           "radiantTeamName":"CREEP","direTeamName":"VP",
#           "leagueID":13404,"endTimeUTC":1629551145}

# [{"type":"PicksAndBans","cName":["npc_dota_hero_visage","npc_dota_hero_dazzle","npc_dota_hero_chen","npc_dota_hero_viper","npc_dota_hero_puck","npc_dota_hero_tiny","npc_dota_hero_winter_wyvern","npc_dota_hero_death_prophet","npc_dota_hero_enigma","npc_dota_hero_tusk","npc_dota_hero_night_stalker","npc_dota_hero_marci","npc_dota_hero_lycan","npc_dota_hero_phoenix","npc_dota_hero_bane","npc_dota_hero_warlock","npc_dota_hero_rattletrap","npc_dota_hero_beastmaster","npc_dota_hero_bloodseeker","npc_dota_hero_spectre","npc_dota_hero_furion","npc_dota_hero_luna","npc_dota_hero_alchemist","npc_dota_hero_razor"],"eName":["CDOTA_Unit_Hero_Visage","CDOTA_Unit_Hero_Dazzle","CDOTA_Unit_Hero_Chen","CDOTA_Unit_Hero_Viper","CDOTA_Unit_Hero_Puck","CDOTA_Unit_Hero_Tiny","CDOTA_Unit_Hero_Winter_Wyvern","CDOTA_Unit_Hero_DeathProphet","CDOTA_Unit_Hero_Enigma","CDOTA_Unit_Hero_Tusk","CDOTA_Unit_Hero_NightStalker","CDOTA_Unit_Hero_Marci","CDOTA_Unit_Hero_Lycan","CDOTA_Unit_Hero_Phoenix","CDOTA_Unit_Hero_Bane","CDOTA_Unit_Hero_Warlock","CDOTA_Unit_Hero_Rattletrap","CDOTA_Unit_Hero_Beastmaster","CDOTA_Unit_Hero_Bloodseeker","CDOTA_Unit_Hero_Spectre","CDOTA_Unit_Hero_Furion","CDOTA_Unit_Hero_Luna","CDOTA_Unit_Hero_Alchemist","CDOTA_Unit_Hero_Razor"],"team":[2,3,2,3,2,3,3,2,2,3,2,3,2,3,3,2,2,3,2,3,2,3,2,3],"ID":[92,50,66,47,13,19,112,43,33,100,60,136,77,110,3,37,51,38,4,67,53,48,73,15],"isPick":[false,false,false,false,true,true,true,true,false,false,false,false,false,false,true,true,true,true,false,false,false,false,true,true],"steamID":[76561198047011640,76561198114980808,76561198054420884,76561198085066985,76561197986172872,76561198100554096,76561198157143864,76561198057068811,76561198086478594,76561198087831260],"playerHero":["npc_dota_hero_alchemist","npc_dota_hero_puck","npc_dota_hero_warlock","npc_dota_hero_death_prophet","npc_dota_hero_rattletrap","npc_dota_hero_razor","npc_dota_hero_winter_wyvern","npc_dota_hero_tiny","npc_dota_hero_beastmaster","npc_dota_hero_bane"],"playerName":["天鸽","Abed","Fly","Nightfall 凛","Cr1t-","Tobi","Kataomi`","Stormstormer","SabeRLighT-","Fishman"],"winningTeam":3,"gameMode":2,"matchID":6701482389,"radiantTeamID":39,"direTeamID":8605863,"radiantTeamName":"EG","direTeamName":"Entity","leagueID":14417,"endTimeUTC":1660169714}]

# {"type":"HeroEntity","xPos":[],"yPos":[],"smoked":[],"alive":[],"entIndex":9601967,"unitName":"CDOTA_Unit_Hero_Puck","cName":"npc_dota_hero_puck","entType":"RADIANT","endOfTime":3688,"createdTime":820,"steamid":76561198114980808,"smokeStart":[],"preciseSmokeStartx":[],"preciseSmokeStarty":[],"preciseSmokeEndx":[],"preciseSmokeEndy":[],"kills":2,"killList":{},"deaths":1,"deathList":{},"assists":3,"assistList":{},"denies":2,"denyList":{},"last_hits":203,"last_hitList":{}}

def build_metadata(match_in) -> dict:
    heroentity_template = {"type":"HeroEntity","xPos":[],"yPos":[],"smoked":[],"alive":[],"entIndex":None,
                            "unitName":None,"cName":None,"entType":"Team","endOfTime":None,
                            "createdTime":None,"steamid":None,"smokeStart":[],"preciseSmokeStartx":[],"preciseSmokeStarty":[],
                            "preciseSmokeEndx":[],"preciseSmokeEndy":[],"kills":None,"killList":{},"deaths":None,"deathList":{},"assists":None,
                            "assistList":{},"denies":None,"denyList":{},"last_hits":None,"last_hitList":{}}
    pickban_template = {"type":"PicksAndBans", "cName": [], "team":[], "ID":[], "isPick":[],
                        "steamID":[], "playerHero":[],
                        "winningTeam":None, "gameMode":None, "matchID":None, "leagueID": None, "endTimeUTC":None,
                        "radiantTeamID":None, "direTeamID":None, "radiantTeamName":None, "direTeamName": None,}
    output = [pickban_template]
    try:
        picks_bans = match_in['picks_bans']
        picks_bans.sort(key=lambda x: x['order'], reverse=False)
    except KeyError:
        print("Missing picks_bans")
        picks_bans = {}
    for pb in picks_bans:
        hero_name = pb['hero']['hero_name']
        if hero_name == 'unknown_hero':
            hero = heroByID[int(pb['hero']['hero_id'])]
        pickban_template['cName'].append(hero_name)
        pickban_template['ID'].append(pb['hero']['hero_id'])
        pickban_template['isPick'].append(pb['is_pick'])
        # Dire is 2 and Radiant is 3
        if pb['side'] == 'dire':
            pickban_template['team'].append(2)
        elif pb['side'] == 'radiant':
            pickban_template['team'].append(3)
        else:
            print(f"Invalid side: {pb['side']}")

    try:
        player_picks = match_in['players_minimal']
    except KeyError:
        print("Missing players_minimal")
        player_picks = {}
    for pp in player_picks:
        hero = dict(heroentity_template)
        pickban_template['steamID'].append(pp['steam_account']['id64'])
        hero['steamid'] = pp['steam_account']['id64']

        hero_name = pp['hero']['hero_name']
        if hero_name == 'unknown_hero':
            hero_name = heroByID[int(pp['hero']['hero_id'])]
        pickban_template['playerHero'].append(hero_name)
        hero['unitName'] = hero_name
        hero['cName'] = hero_name
        if pp['side'] == 'dire':
            hero['entType'] = "DIRE"
        elif pp['side'] == 'radiant':
            hero['entType'] = "RADIANT"

        output.append(hero)

    # Winner is different to team, 2 is radiant, 3 is dire to match replays
    try:
        if match_in['winner'] == 'dire':
            pickban_template['winningTeam'] = 3
        elif match_in['winner'] == 'radiant':
            pickban_template['winningTeam'] = 2

        pickban_template['gameMode'] = match_in['game_mode']
        pickban_template['matchID'] = match_in['match_id']
        pickban_template['leagueID'] = match_in['leagueid']
        pickban_template['endTimeUTC'] = match_in['start_time']
        pickban_template['radiantTeamID'] = match_in['radiant_team_id']
        pickban_template['direTeamID'] = match_in['dire_team_id']
        pickban_template['radiantTeamName'] = match_in['radiant_name']
        pickban_template['direTeamName'] = match_in['dire_name']

    except:
        print("Invalid metadata!")

    return output


def save_match_draft(match_in, output_dir: Path = Path(environment['DRAFT_JSON_PATH'])) -> Path:
    res = build_metadata(match_in)
    output = output_dir / f"{match_in['match_id']}.json"
    if output.exists():
        print(f"Warning! f{output} already exists!")
    with open(output, "w") as f:
        dump(res, f)

    return output
