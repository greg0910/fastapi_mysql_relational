from fastapi import FastAPI
from app.routers.user import router as user_router

from .db.db import engine, Base
from .models import user

app = FastAPI()
app.include_router(user_router)
Base.metadata.create_all(bind=engine)