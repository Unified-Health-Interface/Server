from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    full_name: Mapped[str] = mapped_column(String, nullable=False)

    allergies: Mapped[list["Allergy"]] = relationship()
    appointments: Mapped[list["Appointment"]] = relationship()
    basic_health: Mapped["BasicHealth"] = relationship()
    bills: Mapped[list["Bill"]] = relationship()
    doctor_notes: Mapped[list["DoctorNote"]] = relationship()
    emergency_contacts: Mapped[list["EmergencyContact"]] = relationship()
    prescriptions: Mapped[list["Prescription"]] = relationship()
    vaccinations: Mapped[list["Vaccination"]] = relationship()
