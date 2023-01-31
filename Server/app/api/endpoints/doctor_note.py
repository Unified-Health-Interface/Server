from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import create_doctor_note, read_user_doctor_note
from app.db import get_db
from app.schemas import DoctorNote, DoctorNoteCreate

router = APIRouter()


@router.post("/", response_model=DoctorNote)
async def create(*, db: Session = Depends(get_db), doctor_note: DoctorNoteCreate):
    return create_doctor_note(db, doctor_note=doctor_note)


@router.get("/{username}", response_model=list[DoctorNote])
async def read(*, db: Session = Depends(get_db), username: str):
    return read_user_doctor_note(db, username)
