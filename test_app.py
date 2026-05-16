import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    """Test that the home page returns 200."""
    response = client.get('/')
    assert response.status_code == 200


def test_home_contains_hello(client):
    """Test that the response contains 'Hello!'."""
    response = client.get('/')
    assert b'Hello!' in response.data


def test_home_contains_date(client):
    """Test that the response contains date info."""
    response = client.get('/')
    assert b'Current date is:' in response.data


def test_home_contains_time(client):
    """Test that the response contains time info."""
    response = client.get('/')
    assert b'Current time is:' in response.data
