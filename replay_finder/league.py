from datetime import datetime, timedelta
from time import sleep

from dota2api import Initialise
from dota2api.src.exceptions import APIError, APITimeoutError
from requests import Session as requests_Session
from sqlalchemy import exists
from sqlalchemy.exc import SQLAlchemyError

from .__init__ import WEB_API_LIMIT
from .api_usage import DecoratorUsageCheck
from .exceptions import APIOverLimit
from .model import League, LeagueStatus, Replay, get_api_usage, make_replay

LEAGUE_EXPIRED_AFTER_DAYS = 30


def update_league_listing(session, extra=None):
    @DecoratorUsageCheck(session, get_api_usage, WEB_API_LIMIT)
    def _update_league():
        dota2_webapi = Initialise()
        return dota2_webapi.get_league_listing()

    try:
        leagues = _update_league()
    except (APIError, APITimeoutError) as e:
        print("Failed to update league listing.")
        print(e)
        return
    except APIOverLimit as e:
        print(e)
        return
    finally:
        sleep(1)

    league_ids = [l['leagueid'] for l in leagues['leagues']]
    if extra is not None:
        league_ids += extra

    for league_id in league_ids:
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
        except SQLAlchemyError as e:
            print("Failed to add new league {}".format(league_id))
            print(e)
            session.rollback()


def get_most_recent(session, league_id):
    # Protects against leagues with 0 replays
    if session.query(Replay).filter(Replay.league_id == league_id).count() == 0:
        return None, None

    replay, time = session.query(Replay.replay_id, Replay.start_time)\
                          .filter(Replay.league_id == league_id)\
                          .order_by(Replay.replay_id.desc())\
                          .first()

    return replay, time


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

    @DecoratorUsageCheck(session, get_api_usage, WEB_API_LIMIT)
    def _get_replays(web_query):
        return dota2_webapi.get_match_history(**web_query)

    def _query_replays(web_query):
        try:
            request = _get_replays(web_query)
        except (APIError, APITimeoutError) as e:
            print("Failed to update league listing.")
            print(e)
            return None, None, None
        except APIOverLimit as e:
            print(e)
            return None, None, None
        finally:
            sleep(1)
        total = request['total_results']
        replays = request['matches']
        processed = len(replays)
        if processed == 0:
            last_replay = 0
            return total, processed, last_replay
        else:
            last_replay = replays[-1]['match_id']

        for r in replays:
            replay_id = r['match_id']
            if session.query(exists().where(Replay.replay_id == replay_id)).scalar():
                continue
            new_replay = make_replay(r)
            new_replay.league_id = league_id
            try:
                session.add(new_replay)
                #session.commit()
            except SQLAlchemyError as e:
                print("Failed to add new match {}".format(replay_id))
                print(e)
                session.rollback()

        return total, processed, last_replay

    processed = 0
    total = 1
    with requests_Session() as r_session:
        dota2_webapi = Initialise(executor=r_session.get)
        while total > processed:
            total, p_in, last_replay = _query_replays(web_query)
            if total is None:
                break
            processed += p_in
            web_query = {'league_id': league_id,
                        'start_at_match_id': last_replay - 1}

    replay, time = get_most_recent(session, league_id)

    league.last_replay = replay
    league.last_replay_time = time
    league.last_update = datetime.now()
    try:
        session.merge(league)
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()

    check_league_expiry(session, league_id)


def check_league_expiry(session, league_id):
    league = session.query(League).filter(League.league_id == league_id).one()
    if league.status == LeagueStatus.FOREVER:
        return

    cutoff = datetime.now() - timedelta(days=LEAGUE_EXPIRED_AFTER_DAYS)

    if league.last_replay_time is None:
        league.status = LeagueStatus.ONGOING
    elif league.last_replay_time > cutoff:
        league.status = LeagueStatus.ONGOING
    else:
        league.status = LeagueStatus.FINISHED
        print("League {} considered finished.".format(league_id))

    try:
        session.merge(league)
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()

    return league.status
