import pytest
from app import add, app

# ----------- Function tests -----------
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-2, -3) == -5

# ----------- API tests -----------
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test health check endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "DevOps app is running"

def test_add_endpoint(client):
    """Test /add endpoint"""
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json["result"] == 5

def test_add_invalid(client):
    """Test /add endpoint with invalid input"""
    response = client.get("/add?a=foo&b=3")
    assert response.status_code == 400
    assert "error" in response.json