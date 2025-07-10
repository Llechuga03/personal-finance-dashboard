from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str

# This is for POST or PUT requests
class CategoryCreate(CategoryBase):
    pass

# This is for GET responses
class CategoryRead(CategoryBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
