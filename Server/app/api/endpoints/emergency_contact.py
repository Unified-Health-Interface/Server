from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import create_emergency_contact, read_user_emergency_contact
from app.db import get_db
from app.schemas import EmergencyContact, EmergencyContactCreate

router = APIRouter()


@router.post("/", response_model=EmergencyContact)
async def create(*, db: Session = Depends(get_db), emergency_contact: EmergencyContactCreate):
    return create_emergency_contact(db, emergency_contact=emergency_contact)


@router.get("/{username}", response_model=list[EmergencyContact])
async def read(*, db: Session = Depends(get_db), username: str):
    return read_user_emergency_contact(db, username)
