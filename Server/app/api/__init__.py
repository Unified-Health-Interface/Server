from fastapi import APIRouter

from app.api.endpoints import allergy, user, vaccination, basic_health, appointment, prescription, bill

api_router = APIRouter()
api_router.include_router(allergy.router, prefix="/allergy", tags=["allergy"])
api_router.include_router(appointment.router, prefix="/appointment", tags=["appointment"])
api_router.include_router(basic_health.router, prefix="/basic-health", tags=["basic-health"])
api_router.include_router(bill.router, prefix="/bill", tags=["bill"])
api_router.include_router(prescription.router, prefix="/prescription", tags=["prescription"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(vaccination.router, prefix="/vaccination", tags=["vaccination"])
