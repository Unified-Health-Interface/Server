from app.crud import create_allergy, read_user_allergies
from app.db import get_db
from app.schemas import Allergy, AllergyCreate, UserIn
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Allergy)
async def create(*, db: Session = Depends(get_db), allergy: AllergyCreate):
    return create_allergy(db, allergy=allergy)


@router.get("/{username}", response_model=list[Allergy])
async def read(*, db: Session = Depends(get_db), username: str):
    return read_user_allergies(db, username)
