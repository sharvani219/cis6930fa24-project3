import pytest
from src.app import app

@pytest.fixture
def client():
    """A pytest fixture that provides a test client."""
    app.testing = True
    with app.test_client() as client:
        yield client

# Test if the index route is working
def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Upload PDF" in response.data  

# Test the visualization page
def test_visualization(client):
    response = client.get("/visualization")
    assert response.status_code == 200
    assert b"Clustering" in response.data  


