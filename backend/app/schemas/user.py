from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserBase(BaseModel):
    name: str 
    email: EmailStr

# This is for POST or PUT requests
class UserCreate(UserBase):
    password: str

# This is for GET responses
class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True