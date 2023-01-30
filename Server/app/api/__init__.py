from fastapi import APIRouter

from app.api.endpoints import allergy, user

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user")
api_router.include_router(allergy.router, prefix="/allergy")
