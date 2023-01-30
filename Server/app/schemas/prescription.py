import datetime

from pydantic import BaseModel


class PrescriptionBase(BaseModel):
    doctor: str | None = None
    medicines: str | None = None
    date: datetime.date | None = None
    done: bool | None = None


class PrescriptionCreate(PrescriptionBase):
    doctor: str
    medicines: str
    date: datetime.date
    done: bool
    username: str


class PrescriptionInDBBase(PrescriptionBase):
    id: int

    class Config:
        orm_mode = True


class Prescription(PrescriptionInDBBase):
    pass
