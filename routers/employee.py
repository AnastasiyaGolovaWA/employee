from fastapi import APIRouter

from schemas.employee import EmployeeDetailsModel, EmployeeModel
from utils import employee as employee_utils

router = APIRouter()


@router.post("/employees", response_model=EmployeeDetailsModel, status_code=201)
async def create_employee(employee: EmployeeModel):
    employee = await employee_utils.create_employee(employee)
    return employee


@router.get("/employees/{employee_id}", response_model=EmployeeDetailsModel)
async def get_employee(employee_id: int):
    return await employee_utils.get_employee(employee_id)
