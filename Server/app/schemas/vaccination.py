import datetime

from pydantic import BaseModel


class VaccinationBase(BaseModel):
    vaccine: str | None = None
    date: datetime.date | None = None


class VaccinationCreate(VaccinationBase):
    vaccine: str
    date: datetime.date
    username: str


class VaccinationInDBBase(VaccinationBase):
    id: int

    class Config:
        orm_mode = True


class Vaccination(VaccinationInDBBase):
    pass
