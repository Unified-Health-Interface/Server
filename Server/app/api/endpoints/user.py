from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import create_user, get_user_by_username
from app.db import get_db
from app.schemas import User, UserCreate

router = APIRouter()


@router.post("/", response_model=User)
async def create(*, db: Session = Depends(get_db), user: UserCreate):
    db_user = get_user_by_username(db, user.username)

    if db_user:
        raise HTTPException(
            status_code=400, detail="A user with this username already exists."
        )

    return create_user(db, user=user)


@router.get("/{username}", response_model=User)
async def read(*, db: Session = Depends(get_db), username: str):
    db_user = get_user_by_username(db, username)

    if db_user is None:
        raise HTTPException(
            status_code=404, detail=f"User with the username {username} does not exist."
        )

    return db_user
