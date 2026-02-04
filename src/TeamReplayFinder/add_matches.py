from os import environ as environment
from TeamReplayFinder.replay_finder.model import InitDB, Replay, ReplayStatus
from sqlalchemy.orm import sessionmaker
import argparse as arg
from TeamReplayFinder.replay_finder.replay_process import add_single_replay

arguments = arg.ArgumentParser()
arguments.add_argument('match_id',
                       help="Match IDs to add to database.",
                       nargs='*')

if __name__ == "__main__":
    args = arguments.parse_args()
    engine = InitDB(environment['REPLAY_LEAGUE_DB_PATH'])
    Session = sessionmaker(bind=engine)
    session = Session()

    limit = 20

    new_ids = []
    query = session.query(Replay)
    print("Adding matches:\n{}.".format(args.match_id))
    for m_id in args.match_id:
        test_q: Replay
        test_q = query.filter(Replay.replay_id == m_id).one_or_none()

        if test_q is None:
            print(f"Adding {m_id}.")
            new_ids.append(str(m_id))
            add_single_replay(session, m_id)
        elif test_q.status is None:
            # Replay was acknowledged but never processed properly
            print(f"Re-Adding {m_id}.")
            new_ids.append(str(m_id))
            add_single_replay(session, m_id)
        else:
            print(f"{m_id} already present in DB.")
    session.commit()

    print(f'All new {len(new_ids)} ids:')
    print(' '.join(new_ids))
