from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False)
    experience = Column(Integer, nullable=False)
    region = Column(String, nullable=False)
