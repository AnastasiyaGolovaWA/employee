from typing import Optional

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    firstName: Optional[str] = 'firstName'
    lastName: Optional[str] = 'lastName'
    email: Optional[str] = ''
    experience: Optional[int] = '0'


class EmployeeDetailsModel(EmployeeBase):
    id: int
    firstName: str
    lastName: str
    email: str
    experience: int

    class Config:
        orm_mode = True
        validate_assignment = True
