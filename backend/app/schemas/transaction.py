from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float
    description: Optional[str] = None
    category_id: int

# This is for POST or PUT requests
class TransactionCreate(TransactionBase):
    pass

# This is for GET responses
class TransactionRead(TransactionBase):
    id: int
    user_id: int
    date: datetime

    class Config:
        orm_mode = True

