from datetime import datetime
from dota2api import convert_to_64_bit
from sqlalchemy import Column, BigInteger, DateTime, Integer, String
from sqlalchemy import ForeignKey, exists, create_engine
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum
from replay_finder import Base
import enum


class Side(enum.Enum):
    DIRE = enum.auto()
    RADIANT = enum.auto()


class ReplayStatus(enum.Enum):
    ACKNOWLEDGED = enum.auto()
    # AQUIRING_URL = enum.auto()
    URL_ACQUIRED = enum.auto()
    DOWNLOADING = enum.auto()
    DOWNLOADED = enum.auto()
    FAILED = enum.auto()


class LeagueStatus(enum.Enum):
    ONGOING = enum.auto()
    FINISHED = enum.auto()
    FORVER = enum.auto()


class Replay(Base):
    __tablename__ = "replays"

    replay_id = Column(BigInteger, primary_key=True)
    start_time = Column(DateTime)
    league_id = Column(Integer)

    process_attempts = Column(Integer)
    replay_url = Column(String)
    status = Column(Enum(ReplayStatus))

    dire_id = Column(Integer)
    radiant_id = Column(Integer)

    players = relationship("Player", cascade="all, delete, delete-orphan")

    @hybrid_method
    def stack_id(self, side):
        p_list = [p.player_id for p in self.players if p.side == side]
        p_list.sort()

        return ''.join(str(p) for p in p_list)

    @hybrid_property
    def dire_stack_id(self):
        return self.stack_id(Side.DIRE)

    @hybrid_property
    def radiant_stack_id(self):
        return self.stack_id(Side.RADIANT)


class Player(Base):
    __tablename__ = "players"

    replay_id = Column(BigInteger, ForeignKey(Replay.replay_id), primary_key=True)
    player_id = Column(BigInteger, primary_key=True)
    hero_id = Column(Integer)
    side = Column(Enum(Side))


def make_replay(dict_obj):
    new_replay = Replay()

    new_replay.replay_id = dict_obj['match_id']
    new_replay.start_time = datetime.fromtimestamp(dict_obj['start_time'])

    new_replay.status = ReplayStatus.ACKNOWLEDGED
    new_replay.process_attempts = 0

    new_replay.dire_id = dict_obj['dire_team_id']
    new_replay.radiant_id = dict_obj['radiant_team_id']

    def _player(p):
        new_player = Player()
        new_player.player_id = convert_to_64_bit(p['account_id'])
        # Works as a bit mask, 8th bit is true if the team is dire
        if p['player_slot'] & 0b10000000 != 0:
            new_player.side = Side.DIRE
        else:
            new_player.side = Side.RADIANT
        new_player.hero_id = p['hero_id']

        return new_player

    new_replay.players = [_player(p) for p in dict_obj['players']]

    return new_replay


class League(Base):
    __tablename__ = "leagues"

    league_id = Column(Integer, primary_key=True)
    last_replay = Column(BigInteger)
    last_replay_time = Column(DateTime)
    last_update = Column(DateTime)
    status = Column(Enum(LeagueStatus))


class WebAPIUsage(Base):
    __tablename__ = "web_api_usage"

    date = Column(DateTime, primary_key=True)
    api_calls = Column(Integer)


def get_api_usage(session):
    today = datetime.today()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)

    query = session.query(WebAPIUsage).filter(WebAPIUsage.date == today).one_or_none()
    if query is None:
        try:
            new_usage = WebAPIUsage(date=today, api_calls=0)
            session.add(new_usage)
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise
        return new_usage

    else:
        return query


class SteamGC_APIUsage(Base):
    __tablename__ = "steamgc_api_usage"

    date = Column(DateTime, primary_key=True)
    api_calls = Column(Integer)


def get_gc_usage(session):
    today = datetime.today()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)

    query = session.query(SteamGC_APIUsage)\
                   .filter(SteamGC_APIUsage.date == today).one_or_none()
    if query is None:
        try:
            new_usage = SteamGC_APIUsage(date=today, api_calls=0)
            session.add(new_usage)
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise
        return new_usage

    else:
        return query


def InitDB(path):
    engine = create_engine(path, echo=False)
    Base.metadata.create_all(engine)

    return engine
