from pydantic import BaseModel


class EmployeeModel(BaseModel):
    firstName: str
    lastName: str
    email: str
    experience: int


class EmployeeDetailsModel(EmployeeModel):
    id: int
    firstName: str
    lastName: str
    email: str
    experience: int
