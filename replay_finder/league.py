from .__init__ import dota2_webapi, WEB_API_LIMIT
from .model import get_api_usage, League, LeagueStatus, make_replay
from .model import Replay
from sqlalchemy import exists
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from dota2api.src.exceptions import APIError, APITimeoutError
from .exceptions import WebAPIOverLimit
from time import sleep
from .api_usage import DecoratorUsageCheck


def update_league_listing(session):
    @DecoratorUsageCheck(session)
    def _update_league():
        return dota2_webapi.get_league_listing()

    try:
        leagues = _update_league()
    except (APIError, APITimeoutError) as e:
        print("Failed to update league listing.")
        print(e)
        return
    except WebAPIOverLimit as e:
        print(e)
        return
    finally:
        sleep(1)

    for l in leagues['leagues']:
        league_id = l['leagueid']
        if session.query(exists().where(League.league_id == league_id)).scalar():
            continue

        new_league = League()
        new_league.league_id = league_id
        new_league.last_replay = 0
        # Probably a better way to do this but not important
        new_league.last_replay_time = datetime(year=1, month=1, day=1)
        new_league.last_update = datetime(year=1, month=1, day=1)
        new_league.status = LeagueStatus.ONGOING

        try:
            session.add(new_league)
            session.commit()
        except SQLAlchemyError as e:
            print("Failed to add new league {}".format(league_id))
            print(e)
            session.rollback()


def update_league_replays(session, league_id):
    api_usage = get_api_usage(session)

    if api_usage.api_calls > WEB_API_LIMIT:
        print("Update aborted due to exceeding API limit!")
        return None

    league = session.query(League).filter(League.league_id == league_id).one()
    if league.status == LeagueStatus.FINISHED:
        print("League {} considered finished.".format(league_id))
        return None

    last_replay = league.last_replay
    if last_replay == 0 or last_replay is None:
        web_query = {'league_id': league_id}
    else:
        web_query = {'league_id': league_id,
                     'start_at_match_id': last_replay}

    @DecoratorUsageCheck(session)
    def _get_replays(web_query):
        return dota2_webapi.get_match_history(**web_query)

    def _query_replays(web_query):
        try:
            request = _get_replays(web_query)
        except (APIError, APITimeoutError) as e:
            print("Failed to update league listing.")
            print(e)
            return None, None, None
        except WebAPIOverLimit as e:
            print(e)
            return None, None, None
        finally:
            sleep(1)
        total = request['total_results']
        replays = request['matches']
        processed = len(replays)
        last_replay = replays[-1]['match_id']

        for r in replays:
            replay_id = r['match_id']
            if session.query(exists().where(Replay.replay_id == replay_id)).scalar():
                continue
            new_replay = make_replay(r)
            try:
                session.add(new_replay)
                session.commit()
            except SQLAlchemyError as e:
                print("Failed to add new match {}".format(replay_id))
                print(e)
                session.rollback()

        return total, processed, last_replay

    processed = 0
    total = 1
    while total > processed:
        total, p_in, last_replay = _query_replays(web_query)
        if total is None:
            break
        processed += p_in
        web_query = {'league_id': league_id,
                     'start_at_match_id': last_replay - 1}
