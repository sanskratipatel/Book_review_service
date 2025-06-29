def test_signup(client):
    res = client.post("/auth/signup", json={"username": "testuser", "password": "secret"})
    assert res.status_code == 200
    assert res.json()["msg"] == "User created"

def test_login(client):
    res = client.post("/auth/token", data={"username": "testuser", "password": "secret"})
    assert res.status_code == 200
    assert "access_token" in res.json()

def test_signup_success(client):
    res = client.post("/auth/signup", json={"username": "testuser1", "password": "secret"})
    assert res.status_code == 200
    assert res.json()["msg"] == "User created"

def test_signup_existing_user(client):
    client.post("/auth/signup", json={"username": "testuser2", "password": "secret"})
    res = client.post("/auth/signup", json={"username": "testuser2", "password": "secret"})
    assert res.status_code == 400

def test_login_invalid(client):
    res = client.post("/auth/token", data={"username": "nouser", "password": "wrong"})
    assert res.status_code == 401
