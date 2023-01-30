from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    full_name: Mapped[str] = mapped_column(String, nullable=False)

    allergies: Mapped[list["Allergy"]] = relationship()
    vaccinations: Mapped[list["Vaccination"]] = relationship()
    basic_health: Mapped["BasicHealth"] = relationship()
    appointments: Mapped[list["Appointment"]] = relationship()
    prescriptions: Mapped[list["Prescription"]] = relationship()
    bills: Mapped[list["Bill"]] = relationship()
