from sqlalchemy import Column, String, Integer
from app.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    full_name = Column(String, nullable=False)
