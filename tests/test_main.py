from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ✅ 1. Happy Path (valid input)
def test_create_user_valid():
    response = client.post("/users", json={"name": "Audith"})
    assert response.status_code == 200
    assert response.json()["name"] == "Audith"


# ❌ 2. Empty name
def test_create_user_empty_name():
    response = client.post("/users", json={"name": ""})
    assert response.status_code == 422


# ❌ 3. Missing field
def test_create_user_missing_name():
    response = client.post("/users", json={})
    assert response.status_code == 422


# ❌ 4. Invalid data type
def test_create_user_invalid_type():
    response = client.post("/users", json={"name": 123})
    assert response.status_code == 422


# ⚠️ 5. Edge case (very long name)
def test_create_user_long_name():
    long_name = "A" * 1000
    response = client.post("/users", json={"name": long_name})
    assert response.status_code == 200  # or 422 depending on your validation


# ⚠️ 6. Duplicate user (depends on your logic)
def test_create_user_duplicate():
    client.post("/users", json={"name": "Audith"})
    response = client.post("/users", json={"name": "Audith"})
    
    # adjust based on your app logic
    assert response.status_code in [200, 400]


# ✅ 7. Get users list
def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# ✅ 8. Check user actually saved
def test_user_persisted():
    client.post("/users", json={"name": "TestUser"})
    response = client.get("/users")
    
    names = [user["name"] for user in response.json()]
    assert "TestUser" in names