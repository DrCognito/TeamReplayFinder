from os import environ as environment

from sqlalchemy import (BigInteger, Column, DateTime, Integer, String,
                        create_engine)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

Base_TI = declarative_base()


class TeamInfo(Base_TI):
    __tablename__ = "team_info"
    team_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    last_change = Column(DateTime)

    players = relationship("TeamPlayer")

    @hybrid_property
    def stack_id(self):
        p_list = [p.payer_id for p in self.players]
        p_list.sort()

        return ''.join(str(p) for p in p_list)


class TeamPlayer(Base_TI):
    __tablename__ = "team_players"
    player_id = Column(BigInteger, primary_key=True)
    name = Column(String)


def InitTeamDB(path=None):
    if path is None:
        path = environment("TEAM_DB_PATH")
    engine = create_engine(path, echo=False)
    Base_TI.metadata.create_all(engine)

    return engine


def build_team(team_id, name, date, players, session):
    new_team = TeamInfo()

    new_team.team_id = team_id
    new_team.name = name
    new_team.date = date
    new_team.players = players

    try:
        session.merge(new_team)
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
        raise

    return new_team


def process_player(name, player_id, session):
    # Check if they exist already, players can be on multiple teams!
    player = session.query(TeamPlayer).filter(TeamPlayer.player_id == player_id)\
                                      .one_or_none()

    if player is None:
        player = TeamPlayer()
        player.player_id = player_id
        player.name = name

        try:
            session.add(player)
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise

    return player


def import_from_old(team_ids, all_players, validity_times):
    for name in team_ids:
        if name not in players:
            print("Player data for {} missing!".format(name))
            continue
