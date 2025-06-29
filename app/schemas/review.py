from pydantic import BaseModel, Field, conint
from pydantic.config import ConfigDict

class ReviewBase(BaseModel):
    content: str = Field(..., min_length=5)
    rating: conint(ge=1, le=5)

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)  # ✅ For SQLAlchemy ORM objects
