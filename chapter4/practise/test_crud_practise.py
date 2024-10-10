"""Testing SQLAlchemy Helper Functions"""
import pytest
from datetime import date

import practise_crud
from practise_database import SessionLocal

# use a test date of 4/1/2024 to test the min_last_changed_date
test_date = date(2024,4,1)

@pytest.fixture(scope="function")
def db_session():
    """This starts a database session and closes it when done"""
    session = SessionLocal()
    yield session
    session.close()

def test_get_player(db_session):
    """Tests you can get the first player"""
    player = practise_crud.get_player(db_session, player_id=1001)
    assert player.player_id == 1001

def test_get_players(db_session):
    """Tests that the count of players in the database is what is expected"""
    players = practise_crud.get_players(db_session, skip=0, limit=10000, min_last_changed_date=test_date)
    print(f"count of returned players is: {players}")
    assert len(players) == 1018

def test_get_players_by_name(db_session):
    """Tests that the count of players in the database is what is expected"""
    players = practise_crud.get_players(db_session, first_name="Bryce", last_name="Young")
    assert len(players)==1
    assert players[0].player_id == 2009

def test_get_all_performances(db_session):
    """Test that the count of performances in the database is what is expected - all the performances"""
    performances = practise_crud.get_performances(db_session, skip=0, limit=18000)
    assert len(performances) == 17306

def test_get_new_performances(db_session):
    """Tests that the count of performances in the database is what is expected"""
    performances = practise_crud.get_performances(db_session, skip=0, limit=10000, min_last_changed_date=test_date)
    assert len(performances) == 2711

def test_get_league(db_session):
    """Tests you can get a league"""
    league = practise_crud.get_league(db_session, league_id = 5002)
    assert league.league_id == 5002
    assert len(league.teams) == 8



def test_get_leagues(db_session):
    """Tests that the count of leagues in the database is what is expected"""
    leagues = practise_crud.get_leagues(db_session, skip=0, limit=10000, min_last_changed_date=test_date)
    assert len(leagues) == 5


def test_get_teams(db_session):
    """Tests that the count of teams in the database is what is expected"""
    teams = practise_crud.get_teams(db_session, skip=0, limit=10000, min_last_changed_date=test_date)
    assert len(teams) == 20

def test_get_teams_for_one_league(db_session):
    """Tests that the count of teams in the database is what is expected"""
    teams = practise_crud.get_teams(db_session, league_id=5001)
    assert len(teams) == 12
    assert teams[0].league_id == 5001

def test_get_team_players(db_session):
    """Tests that a team record can retrieve players, and that 8 players are on the first team"""
    first_team = practise_crud.get_teams(db_session, skip=0, limit=1000, min_last_changed_date=test_date)[0]
    assert len(first_team.players) == 7

# test the count functions
def test_get_player_count(db_session):
    player_count = practise_crud.get_player_count(db_session)
    assert player_count == 1018

def test_get_team_count(db_session):
    team_count = practise_crud.get_team_count(db_session)
    assert team_count == 20

def test_get_league_count(db_session):
    league_count = practise_crud.get_league_count(db_session)
    assert league_count == 5
