import time
from os import environ as environment
from typing import List, Tuple
from replay_finder.model import InitDB, Replay
import bs4
import requests as r
from sqlalchemy.orm import sessionmaker
import argparse as arg
from random import randrange

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"
base_url = "https://www.dotabuff.com/esports/teams/"


cache_id = {}
def get_team_url(team_id: int) -> str:
    """Returns a dotabuff team url for team_id.
    Follow the redirect so we behave like a client.

    Arguments:
        team_id {int} -- Team ID number.

    Returns:
        str -- Url for team_id.
    """
    if team_id in cache_id:
        return cache_id[team_id]
    test_url = "{}{}".format(base_url, team_id)
    headers = {
        'User-Agent': user_agent
    }
    try:
        response = r.get(test_url, headers=headers)
        time.sleep(randrange(1, 5))
        response.raise_for_status()
    except r.HTTPError:
        print("Failed to retrieve {} with {}".format(url, params))
        raise

    if response.history:
        print("Team {} redirected to {}".format(team_id, response.url))
        cache_id[team_id] = response.url
        return response.url
    else:
        cache_id[team_id] = test_url
        return test_url


def get_match_url(team_id: int, page: int = 1,
                  faction: str = None) -> Tuple[str, dict]:
    """Get the match url for team_id at page and for faction.

    Arguments:
        team_id {int} -- Team ID number.

    Keyword Arguments:
        page {int} -- Match results page number. (default: {1})
        faction {str} -- Faction, radiant or dire. (default: {None})

    Returns:
        Tuple[str, dict] -- Url and parameter dictionary for requests.
    """
    assert(faction in [None, 'dire', 'radiant'])

    team_url = get_team_url(team_id)
    match_url = "{}/matches".format(team_url)
    params = {
        'page': page,
    }

    if faction:
        params['faction'] = faction

    return (match_url, params)


def get_page(url: str, params: dict) -> str:
    """Gets page using requests.

    Arguments:
        url {str} -- URL
        params {dict} -- Parameters

    Returns:
        str -- Html string for the soup.
    """
    headers = {
        'User-Agent': user_agent
    }
    try:
        response = r.get(url, params=params, headers=headers)
        time.sleep(randrange(1, 5))
        response.raise_for_status()
    except r.HTTPError:
        print("Failed to retrieve {} with {}".format(url, params))
        raise

    return response.text


def matches_from_page(soup: bs4.BeautifulSoup) -> List[int]:
    """Get a list of matches from the soup. Sorted by id.
    
    Arguments:
        soup {bs4.BeautifulSoup} -- Beautifulsoup object for match page.
    
    Returns:
        List[int] -- List of match IDs.
    """
    lost = soup.find_all('a', class_='lost')
    won = soup.find_all('a', class_='won')

    out = []
    for m in lost + won:
        try:
            m_id = m['href'].split('/')[-1]
            out.append(int(m_id))
        except (KeyError, IndexError):
            print("Failed to get url from {}".format(m))
    out.sort(reverse=True)

    return out


arguments = arg.ArgumentParser()
arguments.add_argument('--team_id', help='Team ID',
                       type=int, required=True)

if __name__ == "__main__":
    args = arguments.parse_args()
    engine = InitDB(environment['REPLAY_LEAGUE_DB_PATH'])
    Session = sessionmaker(bind=engine)
    session = Session()

    team_id = args.team_id
    limit = 20

    def _process_side(s: str, page: int = 1) -> List[int]:
        url, params = get_match_url(team_id, page=page, faction=s)
        html = get_page(url, params)
        soup = bs4.BeautifulSoup(html, features="html.parser")
        return matches_from_page(soup)

    dire = _process_side('dire')
    radiant = _process_side('radiant')

    new_ids = []
    query = session.query(Replay.replay_id)
    new = 0
    matched = 0
    for m_id in dire + radiant:
        test_q = query.filter(Replay.replay_id == m_id).one_or_none()

        if test_q is None:
            new += 1
            new_ids.append(str(m_id))
        else:
            matched += 1

    print(' '.join(new_ids))
    print('New: {} Matched: {}'.format(new, matched))
