import datetime

from pydantic import BaseModel


class BasicHealthBase(BaseModel):
    age: int | None = None
    dob: datetime.date | None = None
    sex: str | None = None
    blood_group: str | None = None


class BasicHealthCreate(BasicHealthBase):
    age: int
    dob: datetime.date
    sex: str
    blood_group: str
    username: str


class BasicHealthInDBBase(BasicHealthBase):
    id: int

    class Config:
        orm_mode = True


class BasicHealth(BasicHealthInDBBase):
    pass
