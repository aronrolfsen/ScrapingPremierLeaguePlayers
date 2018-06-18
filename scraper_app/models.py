from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, Float

import scraper_app.settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**scraper_app.settings.DATABASE))


def create_players_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Players(DeclarativeBase):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    team = Column('team', String, nullable=True)
    name = Column('name', String, unique=True)
    age = Column('age', Integer, nullable=True)
    goals = Column('goals', Integer, nullable=True)
    assists = Column('assists', Integer, nullable=True)
    passes = Column('passes', Integer, nullable=True)
    tackles = Column('tackles', Integer, nullable=True)
    position = Column('position', String, nullable=True)
    appearances = Column('appearances', Integer, nullable=True)
    saves = Column('saves', Integer, nullable=True)
    penalties = Column('penalties', Integer, nullable=True)
    punches = Column('punches', Integer, nullable=True)
    highclaims = Column('high claims', Integer, nullable=True)
    catches = Column('catches', Integer, nullable=True)
    sweeperclearances = Column('sweeper clearances', Integer, nullable=True)
    throwouts = Column('throw outs', Integer, nullable=True)
    goalkicks = Column('goal kicks', Integer, nullable=True)
    yellowcards = Column('yellow cards', Integer, nullable=True)
    redcards = Column('red cards', Integer, nullable=True)
    fouls = Column('fouls', Integer, nullable=True)
    cleansheets = Column('clean sheets', Integer, nullable=True)
    goalsconceded = Column('goals conceded', Integer, nullable=True)
    errorsleadingtogoal = Column('errors leading to goal', Integer, nullable=True)
    owngoals = Column('own goals', Integer, nullable=True)
    passespermatch = Column('passes per match', Float, nullable=True)
    accuratelongballs = Column('accurate long balls', Integer, nullable=True)
    goalspermatch = Column('goals per match', Float, nullable=True)
    goalswithheader = Column('goals with header', Integer, nullable=True)
    goalswithrightfoot = Column('goals with right foot', Integer, nullable=True)
    goalswithleftfoot = Column('goals with left foot', Integer, nullable=True)
    penaltiesscored = Column('penalties scored', Integer, nullable=True)
    goalsfromfreekick = Column('goals from freekick', Integer, nullable=True)
    shots = Column('shots', Integer, nullable=True)
    shotsontarget = Column('shots on target', Integer, nullable=True)
    shootingaccuracy = Column('shooting accuracy', String, nullable=True)
    hitwoodwork = Column('hit woodwork', Integer, nullable=True)
    bigchancesmissed = Column('big chances missed', Integer, nullable=True)
    crosses = Column('crosses', Integer, nullable=True)
    bigchancescreated = Column('big chances created', Integer, nullable=True)
    blockedshots = Column('blocked shots', Integer, nullable=True)
    interceptions = Column('interceptions', Integer, nullable=True)
    clearances = Column('clearances', Integer, nullable=True)
    headedclearance = Column('headed clearances', Integer, nullable=True)
    tacklesuccess = Column('tackles success', String, nullable=True)
    recoveries = Column('recoveries', Integer, nullable=True)
    duelswon = Column('duels won', Integer, nullable=True)
    duelslost = Column('duels lost', Integer, nullable=True)
    successful5050s = Column('successful 50/50s', Integer, nullable=True)
    aerialbattleswon = Column('aerial battles won', Integer, nullable=True)
    aerialbattleslost = Column('aerial battles lost', Integer, nullable=True)
    crossaccuracy = Column('cross accuracy', String, nullable=True)
    troughballs = Column('through balls', Integer, nullable=True)
