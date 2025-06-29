import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, get_db
from app.main import app
import redis
from app.db.redis_cache import REDIS_URL

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True, scope="function")
def clear_redis_before_test():
    r = redis.Redis.from_url(REDIS_URL, decode_responses=True)
    r.flushdb()

@pytest.fixture(scope="module")
def client():
    yield TestClient(app)

def get_auth_headers(client):
    client.post("/auth/signup", json={"username": "bookuser", "password": "secret"})
    res = client.post("/auth/token", data={"username": "bookuser", "password": "secret"})
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}