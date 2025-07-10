from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL, EXTRA_DB_ARGS

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, connect_args=EXTRA_DB_ARGS)
# Using this later in routes to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)