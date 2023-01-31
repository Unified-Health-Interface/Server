from pydantic import BaseModel

from app.schemas.allergy import Allergy
from app.schemas.appointment import Appointment
from app.schemas.basic_health import BasicHealth
from app.schemas.bill import Bill
from app.schemas.doctor_note import DoctorNote
from app.schemas.emergency_contact import EmergencyContact
from app.schemas.prescription import Prescription
from app.schemas.vaccination import Vaccination


class UserBase(BaseModel):
    username: str | None = None
    full_name: str | None = None

    allergies: list[Allergy] | None = None
    appointments: list[Appointment] | None = None
    basic_health: BasicHealth | None = None
    bills: list[Bill] | None = None
    doctor_note: list[DoctorNote] | None = None
    emergency_contacts: list[EmergencyContact] | None = None
    prescriptions: list[Prescription] | None = None
    vaccinations: list[Vaccination] | None = None


class UserCreate(UserBase):
    username: str
    full_name: str


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass
