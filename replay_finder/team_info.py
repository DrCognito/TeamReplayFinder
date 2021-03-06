from datetime import datetime, timedelta
from util import convert_to_64_bit
from os import environ as environment

from sqlalchemy import (BigInteger, Column, DateTime, ForeignKey, Integer,
                        String, create_engine)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

Base_TI = declarative_base()
DEFAULT_TIME = datetime.today() - timedelta(days=30)


class TeamInfo(Base_TI):
    __tablename__ = "team_info"
    team_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    last_change = Column(DateTime)
    stack_id = Column(String)

    players = relationship("TeamPlayer",
                           cascade="save-update, merge, "
                                   "delete, delete-orphan")


class TeamPlayer(Base_TI):
    __tablename__ = "team_players"
    player_id = Column(BigInteger, primary_key=True)
    team_id = Column(Integer, ForeignKey(TeamInfo.team_id), primary_key=True)
    name = Column(String)


def InitTeamDB(path=None):
    if path is None:
        path = environment["TEAM_DB_PATH"]
    engine = create_engine(path, echo=False)
    Base_TI.metadata.create_all(engine)

    return engine


def build_team(team_id, name, date, players, session):
    new_team = TeamInfo()

    new_team.team_id = team_id
    new_team.name = name
    new_team.last_change = date
    new_team.players = players

    def _stack_id(team):
        p_list = [p.player_id for p in team.players]
        p_list.sort()

        return ''.join(str(p) for p in p_list)

    new_team.stack_id = _stack_id(new_team)

    try:
        session.merge(new_team)
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
        raise

    return new_team


def update_stack_ids(session):
    teams = session.query(TeamInfo).filter(TeamInfo.stack_id == None)

    for team in teams:
        p_list = [p.player_id for p in team.players]
        p_list.sort()

        team.stack_id = ''.join(str(p) for p in p_list)

        try:
            session.merge(team)
        except SQLAlchemyError:
            session.rollback()


def process_player(name, player_id, team_id, session):

    player = TeamPlayer()
    player.player_id = convert_to_64_bit(player_id)
    player.name = name
    player.team_id = team_id

    try:
        session.merge(player)
        # session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise

    return player


def import_from_old(team_ids, all_players, validity_times, session):
    for name in team_ids:
        if name not in all_players:
            print("Player data for {} missing!".format(name))
            continue

        valid_from = validity_times.get(name, DEFAULT_TIME)

        player_list = []
        team = all_players[name]
        for player in team:
            player_list.append(process_player(player, team[player],
                                              team_ids[name], session))

        build_team(team_ids[name], name, valid_from, player_list, session)
