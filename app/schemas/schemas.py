from typing import Optional

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    firstName: Optional[str] = 'firstName'
    lastName: Optional[str] = 'lastName'
    email: Optional[str] = None
    experience: Optional[int] = 0
    region: Optional[str] = 'Samara'


class EmployeeDetailsModel(EmployeeBase):
    id: int
    firstName: str
    lastName: str
    email: str
    experience: int
    region: str

    class Config:
        orm_mode = True
