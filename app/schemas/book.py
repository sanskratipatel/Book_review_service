from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    description: str

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True) 
