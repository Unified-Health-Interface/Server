import datetime

from pydantic import BaseModel


class VaccinationBase(BaseModel):
    vaccine: str | None = None
    date: datetime.date | None = None
    done: bool | None = None


class VaccinationCreate(VaccinationBase):
    vaccine: str
    date: datetime.date
    username: str
    done: bool


class VaccinationInDBBase(VaccinationBase):
    id: int

    class Config:
        orm_mode = True


class Vaccination(VaccinationInDBBase):
    pass
