import time
from os import environ as environment
from typing import List, Tuple
from TeamReplayFinder.replay_finder.model import InitDB, Replay
import requests as r
from sqlalchemy.orm import sessionmaker
import argparse as arg
from random import randrange, sample
from TeamReplayFinder.replay_finder import DATDOTA_API_LIMIT
from TeamReplayFinder.replay_finder.replay_process import add_single_replay
from TeamReplayFinder.replay_finder.api_usage import APIOverLimit, DecoratorUsageCheck
from TeamReplayFinder.replay_finder.model import get_datdota_usage


base_url = "https://www.dotabuff.com/esports/teams/"


cache_id = {}

def get_json(url: str) -> str:
    """Gets page using requests.

    Arguments:
        url {str} -- URL
        params {dict} -- Parameters

    Returns:
        str -- Html string for the soup.
    """
    # headers = {
    #     'User-Agent': user_agent
    # }
    try:
        response = r.get(url)
        time.sleep(3)
    except r.HTTPError:
        # print("Failed to retrieve {} with {} code {}".format(url, r.status_code))
        print(f"Failed to retrieve {query} with {response.status_code}")
        print(f"Headers:\n{response.headers}")
        response.raise_for_status()
        raise

    return response.json()


def process_team(team_id: int) -> List[int]:
    print(f"Processing team {team_id}")
    url = f"https://datdota.com/api/teams/{team_id}"
    team_json = get_json(url)

    # matches = [x['matchId'] for x in j for j in k['matches'] for k in team_json['data']]
    matches = [x['matchId'] for x in team_json['data']['matches']]

    return matches


arguments = arg.ArgumentParser()
arguments.add_argument('team_id',
                       help="Team ids to retrieve from DotaBuff",
                       nargs='*')


if __name__ == "__main__":
    args = arguments.parse_args()
    engine = InitDB(environment['REPLAY_LEAGUE_DB_PATH'])
    Session = sessionmaker(bind=engine)
    session = Session()

    limit = 80

    new_ids = []
    query = session.query(Replay.replay_id)
    print("Processing {} teams.".format(len(args.team_id)))
    datdota_dec = DecoratorUsageCheck(session, get_datdota_usage, DATDOTA_API_LIMIT)
    process_team = datdota_dec(process_team)
    for t_id in sample(args.team_id, k=len(args.team_id)):
        ids = process_team(t_id)
        new = 0
        matched = 0
        new_team = []
        for m_id in ids[:limit]:
            test_q = query.filter(Replay.replay_id == m_id).one_or_none()

            if test_q is None:
                print(f"Adding {m_id}.")
                new += 1
                new_team.append(str(m_id))
                add_single_replay(session, m_id)
            else:
                matched += 1
        print('Team: {}'.format(t_id))
        if new_team:
            print(' '.join(new_team))
        print('New: {} Matched: {}\n'.format(new, matched))
        new_ids += new_team
        session.commit()

    print(f'All new {len(new_ids)} ids:')
    new_ids = set(new_ids)
    print(' '.join(new_ids))