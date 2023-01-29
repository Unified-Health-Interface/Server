from app.crud import create_user
from app.db import get_db
from app.schemas import User, UserCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=User)
async def create(*, db: Session = Depends(get_db), user: UserCreate):
    db_user = create_user(db, user=user)
    return db_user
