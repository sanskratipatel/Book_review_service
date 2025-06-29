
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.book import BookCreate, BookOut
from app.schemas.review import ReviewCreate, ReviewOut
from app.crud import books as books_crud
from app.crud import review as reviews_crud
from app.db.redis_cache import get_cached_books, set_cached_books
from app.api.auth import get_current_user
import json

router = APIRouter()


@router.get("/books", response_model=list[BookOut])
async def list_books(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        cached = await get_cached_books() 
        if cached:
            return json.loads(cached)
        books = books_crud.get_books(db)
        data = [BookOut.from_orm(book).dict() for book in books]
        await set_cached_books(json.dumps(data))
        return data 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list books: {e}")



@router.post("/books", response_model=BookOut)
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        return books_crud.create_book(db, book)  # ✅ NO `with db.begin()`
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to add book: {e}")


# ✅ Get reviews of a book (auth required)
@router.get("/books/{book_id}/reviews", response_model=list[ReviewOut])
def get_reviews(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        return reviews_crud.get_reviews_by_book(db, book_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Reviews not found: {e}")


# ✅ Add a review to a book (transaction + auth)
@router.post("/books/{book_id}/reviews", response_model=ReviewOut)
def add_review(
    book_id: int,
    review: ReviewCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
       
            return reviews_crud.create_review(db, book_id, review)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to add review: {e}")
