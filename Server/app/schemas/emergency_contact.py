from pydantic import BaseModel


class EmergencyContactBase(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None


class EmergencyContactCreate(EmergencyContactBase):
    name: str
    email: str
    phone: str
    username: str


class EmergencyContactInDBBase(EmergencyContactBase):
    id: int

    class Config:
        orm_mode = True


class EmergencyContact(EmergencyContactInDBBase):
    pass
