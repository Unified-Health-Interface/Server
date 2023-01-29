from app.api.endpoints import user
from app.db import get_db
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user")
