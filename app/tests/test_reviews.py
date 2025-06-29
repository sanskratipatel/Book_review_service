import pytest
from app.tests.utils import get_auth_headers  # ✅ import helper function

def test_add_review(client):
    headers = get_auth_headers(client)

    # Add a book first
    book_res = client.post(
        "/books",
        json={"title": "Ramayana", "author": "Valmiki", "description": "An ancient Indian epic"},
        headers=headers
    )
    assert book_res.status_code == 200, f"Book creation failed: {book_res.text}"
    book = book_res.json()

    # Add a review
    review_res = client.post(
        f"/books/{book['id']}/reviews",
        json={"content": "Epic!", "rating": 5},
        headers=headers
    )
    assert review_res.status_code == 200, f"Review creation failed: {review_res.text}"
    assert review_res.json()["rating"] == 5
    assert review_res.json()["content"] == "Epic!"

def test_get_reviews(client):
    headers = get_auth_headers(client)

    # Add a book first
    book_res = client.post(
        "/books",
        json={"title": "Mahabharata", "author": "Vyasa", "description": "Another ancient epic"},
        headers=headers
    )
    assert book_res.status_code == 200, f"Book creation failed: {book_res.text}"
    book = book_res.json()

    # Add a review
    review_res = client.post(
        f"/books/{book['id']}/reviews",
        json={"content": "Intense story", "rating": 4},
        headers=headers
    )
    assert review_res.status_code == 200, f"Review creation failed: {review_res.text}"

    # Get reviews
    get_res = client.get(f"/books/{book['id']}/reviews", headers=headers)
    assert get_res.status_code == 200, f"Fetching reviews failed: {get_res.text}"
    reviews = get_res.json()
    assert isinstance(reviews, list)
    assert any(r["content"] == "Intense story" for r in reviews)


def test_add_review_success(client):
    headers = get_auth_headers(client)
    book = client.post("/books", json={"title": "Ramayana", "author": "Valmiki", "description": "Epic"}, headers=headers).json()
    review = {"content": "Amazing read", "rating": 5}
    res = client.post(f"/books/{book['id']}/reviews", json=review, headers=headers)
    assert res.status_code == 200
    assert res.json()["rating"] == 5

def test_add_review_invalid_rating(client):
    headers = get_auth_headers(client)
    book = client.post("/books", json={"title": "Test", "author": "Test", "description": "Test"}, headers=headers).json()
    review = {"content": "Bad", "rating": 10}  # invalid rating
    res = client.post(f"/books/{book['id']}/reviews", json=review, headers=headers)
    assert res.status_code == 422

def test_get_reviews(client):
    headers = get_auth_headers(client)
    book = client.post("/books", json={"title": "Mahabharata", "author": "Vyasa", "description": "Epic"}, headers=headers).json()
    client.post(f"/books/{book['id']}/reviews", json={"content": "Great", "rating": 4}, headers=headers)
    res = client.get(f"/books/{book['id']}/reviews", headers=headers)
    assert res.status_code == 200
    assert any(r["content"] == "Great" for r in res.json())
