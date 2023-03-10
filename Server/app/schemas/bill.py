import datetime

from pydantic import BaseModel


class BillBase(BaseModel):
    hospital: str | None = None
    service: str | None = None
    amount: int | None = None
    due_date: datetime.date | None = None
    paid: bool | None = None


class BillCreate(BillBase):
    hospital: str
    service: str
    amount: int
    due_date: datetime.date
    paid: bool
    username: str


class BillInDBBase(BillBase):
    id: int

    class Config:
        orm_mode = True


class Bill(BillInDBBase):
    pass
