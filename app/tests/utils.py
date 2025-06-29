# app/tests/utils.py
# app/tests/utils.py
def get_auth_headers(client):
    client.post("/auth/signup", json={"username": "testuser", "password": "secret"})
    res = client.post("/auth/token", data={"username": "testuser", "password": "secret"})
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
