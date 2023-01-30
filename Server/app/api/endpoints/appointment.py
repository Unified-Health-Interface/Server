from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import create_appointment, read_user_appointments
from app.db import get_db
from app.schemas import Appointment, AppointmentCreate

router = APIRouter()


@router.post("/", response_model=Appointment)
async def create(*, db: Session = Depends(get_db), appointment: AppointmentCreate):
    return create_appointment(db, appointment=appointment)


@router.get("/{username}", response_model=list[Appointment])
async def read(*, db: Session = Depends(get_db), username: str):
    return read_user_appointments(db, username)
