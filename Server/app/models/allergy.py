from app.db import Base
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Allergy(Base):
    __tablename__ = "allergy"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    allergy: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(ForeignKey("users.username"))


