from app.models.book import Book
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate

def get_books(db: Session):
    return db.query(Book).all()

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.model_dump())  
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
