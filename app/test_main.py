from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add():
    response = client.get("/add?x=5&y=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_subtract():
    response = client.get("/subtract?x=5&y=3")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_multiply():
    response = client.get("/multiply?x=5&y=3")
    assert response.status_code == 200
    assert response.json() == {"result": 15}

def test_divide():
    response = client.get("/divide?x=6&y=3")
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}
