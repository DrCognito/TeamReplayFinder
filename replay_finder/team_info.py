from datetime import datetime, timedelta
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

    players = relationship("TeamPlayer")

    @hybrid_property
    def stack_id(self):
        p_list = [p.player_id for p in self.players]
        p_list.sort()

        return ''.join(str(p) for p in p_list)


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

    try:
        session.merge(new_team)
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
        raise

    return new_team


def process_player(name, player_id, team_id, session):

    player = TeamPlayer()
    player.player_id = player_id
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
