from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import create_basic_health, read_user_basic_health
from app.db import get_db
from app.schemas import BasicHealth, BasicHealthCreate

router = APIRouter()


@router.post("/", response_model=BasicHealth)
async def create(*, db: Session = Depends(get_db), basic_health: BasicHealthCreate):
    return create_basic_health(db, basic_health=basic_health)


@router.get("/{username}", response_model=BasicHealth)
async def read(*, db: Session = Depends(get_db), username: str):
    return read_user_basic_health(db, username)
