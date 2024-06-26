from TeamReplayFinder.replay_finder.match_draft import save_match_draft
from TeamReplayFinder.replay_finder.api_usage import DecoratorUsageCheck
from TeamReplayFinder.replay_finder.__init__ import WEB_API_LIMIT
from TeamReplayFinder.replay_finder.model import get_api_usage, InitDB, make_replay_odota, get_replay_odota
from TeamReplayFinder.replay_finder.match_draft_odota import save_match_draft_odota
import argparse as arg
from os import environ as environment
from sqlalchemy.orm import sessionmaker
import d2api
from time import sleep

arguments = arg.ArgumentParser()
arguments.add_argument('match_id',
                       help="Match IDs to add to database.",
                       nargs='*')


if __name__ == "__main__":
    args = arguments.parse_args()
    engine = InitDB(environment['REPLAY_LEAGUE_DB_PATH'])
    Session = sessionmaker(bind=engine)
    session = Session()
    dota2_webapi = d2api.APIWrapper()

    @DecoratorUsageCheck(session, get_api_usage, WEB_API_LIMIT)
    def _get_replay_details(web_query):
        return dota2_webapi.get_match_details(**web_query)

    for m_id in args.match_id:
        print(f"Adding {m_id}")
        try:
            match_query = _get_replay_details({'match_id': m_id})
            save_match_draft(match_query)
        except(d2api.errors.APITimeoutError, d2api.errors.BaseError) as e:
            print(f"Failed to add {m_id}, valve Dota2 API Time Out.")
            match_query = None
        sleep(1)

        if match_query is None:
            match_query = get_replay_odota(m_id)
            if match_query is None:
                print(f"Failed to add {m_id} from Open Dota.")
            else:
                new_replay = make_replay_odota(match_query)
                save_match_draft_odota(match_query)

