from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import create_prescription, read_user_prescription
from app.db import get_db
from app.schemas import Prescription, PrescriptionCreate

router = APIRouter()


@router.post("/", response_model=Prescription)
async def create(*, db: Session = Depends(get_db), prescription: PrescriptionCreate):
    return create_prescription(db, prescription=prescription)


@router.get("/{username}", response_model=list[Prescription])
async def read(*, db: Session = Depends(get_db), username: str, only_pending: bool = False):
    return read_user_prescription(db, username, only_pending)
