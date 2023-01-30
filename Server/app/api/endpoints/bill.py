from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import create_bill, read_user_bill
from app.db import get_db
from app.schemas import Bill, BillCreate

router = APIRouter()


@router.post("/", response_model=Bill)
async def create(*, db: Session = Depends(get_db), bill: BillCreate):
    return create_bill(db, bill=bill)


@router.get("/{username}", response_model=list[Bill])
async def read(*, db: Session = Depends(get_db), username: str, only_pending: bool = False):
    return read_user_bill(db, username, only_pending)
