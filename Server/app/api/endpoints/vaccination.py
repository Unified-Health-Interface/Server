from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import create_vaccination, read_user_vaccinations
from app.db import get_db
from app.schemas import Vaccination, VaccinationCreate

router = APIRouter()


@router.post("/", response_model=Vaccination)
async def create(*, db: Session = Depends(get_db), vaccination: VaccinationCreate):
    return create_vaccination(db, vaccination=vaccination)


@router.get("/{username}", response_model=list[Vaccination])
async def read(*, db: Session = Depends(get_db), username: str):
    return read_user_vaccinations(db, username)
