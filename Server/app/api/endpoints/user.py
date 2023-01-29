from app.crud import create_user, get_user, get_user_by_username
from app.db import get_db
from app.schemas import User, UserCreate
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=User)
async def create(*, db: Session = Depends(get_db), user: UserCreate):
    db_user = get_user_by_username(db, user.username)

    if db_user:
        raise HTTPException(
            status_code=400, detail="A user with this username already exists."
        )

    return create_user(db, user=user)


@router.get("/{user_id}", response_model=User)
async def read(*, db: Session = Depends(get_db), user_id: int):
    db_user = get_user(db, user_id)

    if db_user is None:
        raise HTTPException(
            status_code=404, detail=f"User with the user id {user_id} does not exist."
        )

    return db_user
