from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users", json={"name": "Audith"})
    assert response.status_code == 200
    assert response.json()["name"] == "Audith"

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)