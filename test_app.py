import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Verifies that the home page loads successfully and contains the correct text"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Pipeline Working Successfully!" in response.data

