import datetime

from pydantic import BaseModel


class AppointmentBase(BaseModel):
    doctor: str | None = None
    hospital: str | None = None
    date_time: datetime.datetime | None = None


class AppointmentCreate(AppointmentBase):
    doctor: str
    hospital: str
    date_time: datetime.datetime
    username: str


class AppointmentInDBBase(AppointmentBase):
    id: int

    class Config:
        orm_mode = True


class Appointment(AppointmentInDBBase):
    pass
