from pydantic import BaseModel


class AllergyBase(BaseModel):
    allergy: str | None = None


class AllergyCreate(AllergyBase):
    allergy: str
    username: str


class AllergyInDBBase(AllergyBase):
    id: int

    class Config:
        orm_mode = True


class Allergy(AllergyInDBBase):
    pass
