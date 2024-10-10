"""SQLAlchemy Query Functions"""
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from datetime import date

import practise_models

def get_player(db: Session, player_id: int):
    return db.query(practise_models.Player).filter(practise_models.Player.player_id == player_id).first()

def get_players(db: Session, skip: int = 0, limit: int = 100, min_last_changed_date: date = None, last_name : str = None, first_name : str = None, ):
    query = db.query(practise_models.Player)
    if min_last_changed_date:
        query = query.filter(practise_models.Player.last_changed_date >= min_last_changed_date)
    if first_name:
        query = query.filter(practise_models.Player.first_name == first_name)
    if last_name:
        query = query.filter(practise_models.Player.last_name == last_name)
    return query.offset(skip).limit(limit).all()


def get_performances(db: Session, skip: int = 0, limit: int = 100, min_last_changed_date: date = None):
    query = db.query(practise_models.Performance)
    if min_last_changed_date:
        query = query.filter(practise_models.Performance.last_changed_date >= min_last_changed_date)
    return query.offset(skip).limit(limit).all()

def get_league(db: Session, league_id: int = None):
    return db.query(practise_models.League).filter(practise_models.League.league_id == league_id).first()

def get_leagues(db: Session, skip: int = 0, limit: int = 100, min_last_changed_date: date = None,league_name: str = None):
    query = db.query(practise_models.League
                    ).options(joinedload(practise_models.League.teams))
    if min_last_changed_date:
        query = query.filter(practise_models.League.last_changed_date >= min_last_changed_date)
    if league_name:
        query = query.filter(practise_models.League.league_name == league_name)
    return query.offset(skip).limit(limit).all()


def get_teams(db: Session, skip: int = 0, limit: int = 100, min_last_changed_date: date = None, team_name: str = None, league_id: int = None):
    query = db.query(practise_models.Team)
    if min_last_changed_date:
        query = query.filter(practise_models.Team.last_changed_date >= min_last_changed_date)
    if team_name:
        query = query.filter(practise_models.Team.team_name == team_name)
    if league_id:
        query = query.filter(practise_models.Team.league_id == league_id)
    return query.offset(skip).limit(limit).all()

#analytics queries
def get_player_count(db: Session):
    query = db.query(practise_models.Player)
    return query.count()

def get_team_count(db: Session):
    query = db.query(practise_models.Team)
    return query.count()

def get_league_count(db: Session):
    query = db.query(practise_models.League)
    return query.count()
