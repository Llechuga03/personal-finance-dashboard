from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

# Base class for the SQLalchemy mocdels
Base = declarative_base()

# USER table
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False) # Hashed password

    categories = relationship("Category", back_populates="user", cascade="all, delete")
    transactions = relationship("Transaction", back_populates="user", cascade="all, delete")    

# CATEGORY table
class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="categories")

    transactions = relationship("Transaction", back_populates="category", cascade="all, delete")

# TRANSACTION table
class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String(255))
    date = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="transactions")

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="transactions")