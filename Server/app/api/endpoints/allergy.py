from app.crud import create_allergy
from app.db import get_db
from app.schemas import Allergy, AllergyCreate, UserIn
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Allergy)
async def create(*, db: Session = Depends(get_db), allergy: AllergyCreate):
    # if db_user:
    #     raise HTTPException(
    #         status_code=400, detail="A user with this username already exists."
    #     )

    return create_allergy(db, allergy=allergy)
