from pydantic import BaseModel


class EmployeeBase(BaseModel):
    firstName: str
    lastName: str
    email: str
    experience: int


class EmployeeDetailsModel(EmployeeBase):
    id: int
    firstName: str
    lastName: str
    email: str
    experience: int
