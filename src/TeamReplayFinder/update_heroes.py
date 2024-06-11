# import dota2api
import d2api
import requests
import time
from dotenv import load_dotenv
from json import dump
from pathlib import Path

output_dir = Path('./heroes')
load_dotenv(dotenv_path="setup.env")
#api = dota2api.Initialise()

api = d2api.APIWrapper()

heroes = api.get_heroes()

dota2_heroimage_url = "http://cdn.dota2.com/apps/dota2/images/heroes/"

hero_map = {}
redownload = False
download = "url_full_portrait"
download_abrev = "_full.png"
for h in heroes['heroes']:
    full_name = h['name']
    print("Processing {}".format(h['name']))
    path: Path = output_dir / (full_name + download_abrev)
    if path.exists() and not redownload:
        print("{} exists and redownload is False".format(path))
        hero_map[full_name] = full_name + download_abrev
        continue
    try:
        url = h[download]
    except KeyError:
        print(f"Missing key {download} for:\n{h}")
        # Have to remove the npc_dota_hero prefix
        hero_name = h['name'].replace('npc_dota_hero_', '')
        url = f"{dota2_heroimage_url}{hero_name}{download_abrev}"
        print(url)
    try:
        r = requests.get(url)
        time.sleep(1)
    except requests.HTTPError:
        print("Failed to retrieve {} at {}".format(full_name, url))
        continue

    with open(path, 'wb') as f:
        f.write(r.content)
        hero_map[full_name] = full_name + download_abrev

out_json = output_dir / "hero_portraits.json"
with open(out_json, 'w') as f:
    dump(hero_map, f)
