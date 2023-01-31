from pydantic import BaseModel


class DoctorNoteBase(BaseModel):
    doctor: str | None = None
    note: str | None = None


class DoctorNoteCreate(DoctorNoteBase):
    doctor: str
    note: str
    username: str


class DoctorNoteInDBBase(DoctorNoteBase):
    id: int

    class Config:
        orm_mode = True


class DoctorNote(DoctorNoteInDBBase):
    pass
