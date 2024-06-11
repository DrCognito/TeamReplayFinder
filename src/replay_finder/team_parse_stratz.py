import time
from os import environ as environment
from typing import List, Tuple
from replay_finder.model import InitDB, Replay
from sqlalchemy.orm import sessionmaker
import argparse as arg

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from datetime import datetime
from replay_finder.replay_process import add_single_replay
from herotools.important_times import ImportantTimes, MAIN_TIME

use_time = MAIN_TIME
STRATZ_KEY = environment['STRATZ_KEY']
stratz_endpoint = AIOHTTPTransport(url=f"https://api.stratz.com/graphql?jwt={STRATZ_KEY}")

# Create a GraphQL client using the defined transport
client = Client(transport=stratz_endpoint, execute_timeout=30)

query = f"""
query MyQuery {{
  team(teamId: TEAM_ID) {{
    matches(request: {{startDateTime: UNIX_START_TIME, skip: 0, take: MAX_REPLAYS}}) {{
      id
    }}
  }}
}}
"""
query = f"""
query MyQuery {{
  team(teamId: TEAM_ID) {{
    matches(request: {{skip: 0, take: MAX_REPLAYS}}) {{
      id
    }}
  }}
}}
"""


def get_team_str(team: int, from_time: datetime, max_replays:int, in_str = query) -> str:
    """Build a team query for stratz gql
    """
    in_str = in_str.replace("TEAM_ID", str(team))
    in_str = in_str.replace("UNIX_START_TIME", str(int(from_time.timestamp())))
    in_str = in_str.replace("MAX_REPLAYS", str(max_replays))

    return in_str


from gql.transport.exceptions import TransportServerError
def process_team(team_id: int, from_time: datetime, max_replays:int) -> List[int]:
    query_str = get_team_str(team_id, from_time, max_replays)
    query = gql(query_str)
    try:
        result = client.execute(query)
    except TransportServerError as e:
        print(f"Raised error/n: {e}")
        print(f"Invalid results for {team_id}, sleeping a bit.")
        time.sleep(5)
        return []
    time.sleep(1)
    try:
        matches = [x['id'] for x in result['team']['matches']]
    except TypeError:
        print(f"Invalid results for {team_id}")
        return []

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

    limit = 40

    new_ids = []
    query = session.query(Replay.replay_id)
    print("Processing {} teams.".format(len(args.team_id)))

    for t_id in args.team_id:
        ids = process_team(t_id, use_time, limit)
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