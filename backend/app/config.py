from dotenv import load_dotenv
import os

load_dotenv()

# Centralizing configuration logic for the application
# Whenever DB connection is needed, it can be imported from this file
DATABASE_URL = os.getenv("DATABASE_URL")

EXTRA_DB_ARGS = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}