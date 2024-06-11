from sqlalchemy import Column, Integer, BigInteger, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pandas import Series, DataFrame
#import .replay
from replay import Replay
from heroTools import heroByID, heroShortName
from math import sqrt

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    match_id = Column(BigInteger, ForeignKey(Replay.match_id),
                      primary_key=True)
    hero_id = Column(Integer, primary_key=True)
    is_pick = Column(Boolean)
    team = Column(Integer)
    order = Column(Integer)


def InitDB(path):
    engine = create_engine(path, echo=False)
    Base.metadata.create_all(engine)

    return engine
