from pydantic import BaseModel, EmailStr


class EmergencyContactBase(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None


class EmergencyContactCreate(EmergencyContactBase):
    name: str
    email: EmailStr
    phone: str
    username: str


class EmergencyContactInDBBase(EmergencyContactBase):
    id: int

    class Config:
        orm_mode = True


class EmergencyContact(EmergencyContactInDBBase):
    pass
