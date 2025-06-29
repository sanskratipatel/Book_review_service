from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    rating = Column(Integer)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)