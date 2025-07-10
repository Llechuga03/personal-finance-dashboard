from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.sessions import SessionLocal
from app.db import models
from app.schemas import user as user_schema
from app.schemas import transaction as transaction_schema
from app.schemas import category as category_schema

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User Endpoints
# Create a new user
@router.post("/users/", response_model=user_schema.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get all users
@router.get("/users/", response_model=list[user_schema.UserRead])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# Category Endpoints
# Create a new category
@router.post("/categories/", response_model=category_schema.CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category(category: category_schema.CategoryCreate, user_id: int, db: Session = Depends(get_db)):
    new_category = models.Category(name=category.name, user_id=user_id)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

# Get all categories for a user
@router.get("/categories/", response_model=list[category_schema.CategoryRead])
def get_categories(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Category).filter(models.Category.user_id == user_id).all()

# Transaction Endpoints
# Create a new transaction
@router.post("/transactions/", response_model=transaction_schema.TransactionRead, status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: transaction_schema.TransactionCreate, user_id: int, db: Session = Depends(get_db)):
    new_transaction = models.Transaction(**transaction.dict(), user_id=user_id)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

# Get all transactions for a user
@router.get("/transactions/", response_model=list[transaction_schema.TransactionRead])
def get_transactions(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()