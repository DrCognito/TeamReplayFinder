import enum
from datetime import datetime

#from dota2api import convert_to_64_bit
from util import convert_to_64_bit
from sqlalchemy import (BigInteger, Column, DateTime, ForeignKey, Integer,
                        String, create_engine, exists, or_, and_)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum

from replay_finder.team_info import TeamInfo


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
    FOREVER = enum.auto()


Base = declarative_base()


class Replay(Base):
    __tablename__ = "replays"

    replay_id = Column(BigInteger, primary_key=True)
    start_time = Column(DateTime)
    league_id = Column(Integer)

    process_attempts = Column(Integer)
    replay_url = Column(String)
    status = Column(Enum(ReplayStatus))
    last_download_time = Column(DateTime)

    dire_id = Column(Integer)
    dire_stack_id = Column(String)
    radiant_id = Column(Integer)
    radiant_stack_id = Column(String)

    players = relationship("Player", cascade="all, delete, delete-orphan")

    def stack_id(self, side):
        p_list = [p.player_id for p in self.players if p.side == side]
        p_list.sort()

        return ''.join(str(p) for p in p_list)


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

    try:
        new_replay.dire_id = dict_obj['dire_team_id']
    except KeyError:
        print("Missing dire team in {}".format(dict_obj['match_id']))
        new_replay.dire_id = 0
    try:
        new_replay.radiant_id = dict_obj['radiant_team_id']
    except KeyError:
        print("Missing radiant team in {}".format(dict_obj['match_id']))
        new_replay.radiant_id = 0

    def _player(p):
        new_player = Player()
        try:
            player_id = p['steam_account']['id64']
        except KeyError as e:
            print("Invalid player object in replay {}."
                  .format(new_replay.replay_id))
            player_id = p['hero']['hero_id']
            raise
            # player_id = p['player_slot']
        new_player.player_id = player_id
        new_player.replay_id = new_replay.replay_id
        # Works as a bit mask, 8th bit is true if the team is dire
        if p['side'] == 'dire':
            new_player.side = Side.DIRE
        elif p['side'] == 'radiant':
            new_player.side = Side.RADIANT
        else:
            raise KeyError('Invalid team! {}'.format(p['side']))
        new_player.hero_id = p['hero']['hero_id']

        return new_player

    new_replay.players = [_player(p) for p in dict_obj['players']]
    new_replay.dire_stack_id = new_replay.stack_id(Side.DIRE)
    new_replay.radiant_stack_id = new_replay.stack_id(Side.RADIANT)

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


class DatDotaAPIUsage(Base):
    __tablename__ = "datdota_api_usage"

    date = Column(DateTime, primary_key=True)
    api_calls = Column(Integer)


def get_datdota_usage(session):
    today = datetime.today()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)

    query = session.query(DatDotaAPIUsage).filter(DatDotaAPIUsage.date == today).one_or_none()
    if query is None:
        try:
            new_usage = DatDotaAPIUsage(date=today, api_calls=0)
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


def update_stack_ids(session):
    r_filter = or_(Replay.dire_stack_id == None,
                   Replay.radiant_stack_id == None)
    replays = session.query(Replay).filter(r_filter)

    for replay in replays:
        replay.dire_stack_id = replay.stack_id(Side.DIRE)
        replay.radiant_stack_id = replay.stack_id(Side.RADIANT)

        try:
            session.merge(replay)
        except SQLAlchemyError:
            session.rollback()


def get_replays_for_team(team: TeamInfo, replay_session, require_both=False):
    team_id = team.team_id
    stack_id = team.stack_id

    if require_both:
        t_filter = and_(or_(Replay.radiant_id == team_id, 
                            Replay.dire_id == team_id),
                        or_(Replay.radiant_stack_id == stack_id,
                        Replay.dire_stack_id == stack_id))
    else:
        t_filter = or_(Replay.radiant_id == team_id, Replay.dire_id == team_id,
                       Replay.radiant_stack_id == stack_id,
                       Replay.dire_stack_id == stack_id)

    return replay_session.query(Replay).filter(t_filter)
