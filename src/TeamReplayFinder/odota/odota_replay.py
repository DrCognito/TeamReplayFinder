from sqlalchemy import Column, Integer, BigInteger, DateTime, Float, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
from json import loads
import datetime

Base = declarative_base()
Patch_7_07 = datetime.datetime(2017, 11, 2, 0, 0, 0, 0)
defaultTime = Patch_7_07


class Replay(Base):
    __tablename__ = "replays"

    match_id = Column(BigInteger, primary_key=True)
    radiant_win = Column(Boolean)
    start_time = Column(DateTime)
    game_mode = Column(Integer)
    dire_team_id = Column(Integer)
    radiant_team_id = Column(Integer)
    leagueid = Column(Integer)
    version = Column(Integer)


def getLatestTime(session):
    try:
        result = session.query(Replay).order_by(Replay.start_time.desc())\
                .first()
    except NoResultFound:
        print("Warning! No results found in database!")
        return defaultTime
    if result is None:
        return defaultTime
    return result.start_time


def getLatestReplayID(session):
    result = session.query(Replay).order_by(Replay.match_id.desc()).first()
    if not result:
        print("Warning no replays present.")
        return 0

    return result.match_id


def InitDB(path):
    engine = create_engine(path, echo=False)
    Base.metadata.create_all(engine)

    return engine
