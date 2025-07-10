from fastapi import FastAPI
from app.api.routes import router

app =FastAPI(title="Personal Finance Tracker API")

app.include_router(router)