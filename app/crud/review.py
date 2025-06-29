# app/crud/review.py

from sqlalchemy.orm import Session
from app.models.review import Review
from app.models.book import Book
from fastapi import HTTPException
from app.schemas.review import ReviewCreate

def get_reviews_by_book(db: Session, book_id: int):
    if not db.query(Book).filter(Book.id == book_id).first():
        raise HTTPException(status_code=404, detail="Book not found")
    return db.query(Review).filter(Review.book_id == book_id).all()

def create_review(db: Session, book_id: int, review: ReviewCreate):
    if not db.query(Book).filter(Book.id == book_id).first():
        raise HTTPException(status_code=404, detail="Book not found")

    db_review = Review(**review.model_dump(), book_id=book_id)  # ✅ Pydantic v2
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
