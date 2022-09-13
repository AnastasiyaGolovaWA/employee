from typing import TypedDict

from sqlalchemy import Column, Integer, String

from database.database import Base


class EmployeeDict(TypedDict):
    firstName: str
    lastName: str
    email: str
    experience: int


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False)
    experience = Column(Integer, nullable=False)

    @property
    def serialize(self) -> EmployeeDict:
        return {"firstName": self.firstName, "lastName": self.lastName, "email": self.email,
                "experience": self.experience}
