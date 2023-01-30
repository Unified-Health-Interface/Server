from fastapi import APIRouter

from app.api.endpoints import allergy, user, vaccination, basic_health, appointment, prescription

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user")
api_router.include_router(allergy.router, prefix="/allergy")
api_router.include_router(vaccination.router, prefix="/vaccination")
api_router.include_router(basic_health.router, prefix="/basic-health")
api_router.include_router(appointment.router, prefix="/appointment")
api_router.include_router(prescription.router, prefix="/prescription")
