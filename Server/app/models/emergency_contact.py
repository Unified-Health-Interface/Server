from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)

    username: Mapped[str] = mapped_column(ForeignKey("users.username"))
