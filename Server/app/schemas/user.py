from app.schemas.allergy import Allergy
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str | None = None
    full_name: str | None = None

    allergies: list[Allergy] | None = None


class UserCreate(UserBase):
    username: str
    full_name: str


class UserIn(UserBase):
    username: str


class UserAllergies(UserBase):
    allergies: list[Allergy]


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass
