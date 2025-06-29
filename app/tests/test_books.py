
# from app.tests.test_books import get_auth_headers
from app.tests.utils import get_auth_headers 
def test_add_book(client):
    headers = get_auth_headers(client)
    res = client.post(
    "/books",
    json={"title": "The Gita", "author": "Krishna", "description": "A spiritual classic"},
    headers=headers
)

    assert res.status_code == 200
    assert res.json()["title"] == "The Gita"

def test_list_books(client):
    headers = get_auth_headers(client)
    res = client.get("/books", headers=headers)
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_add_book_success(client):
    headers = get_auth_headers(client)
    res = client.post("/books", json={"title": "Gita", "author": "Krishna", "description": "Spiritual"}, headers=headers)
    assert res.status_code == 200
    assert res.json()["title"] == "Gita"

def test_add_book_missing_field(client):
    headers = get_auth_headers(client)
    res = client.post("/books", json={"author": "Krishna", "description": "No title"}, headers=headers)
    assert res.status_code == 422

def test_list_books(client):
    headers = get_auth_headers(client)
    res = client.get("/books", headers=headers)
    assert res.status_code == 200
    assert isinstance(res.json(), list)