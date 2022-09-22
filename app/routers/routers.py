from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import engine
from app.functions import get_session
from app.models import employee
from app.schemas.schemas import EmployeeDetailsModel, EmployeeBase
from app.services import employee_service

employee.Base.metadata.create_all(bind=engine)
router = APIRouter()


@router.get("/employees/{firstName}", response_model=EmployeeDetailsModel)
def find_employee_by_firstname(firstName: str, session: Session = Depends(get_session)):
    employee = employee_service.get_employee_by_firstname(session=session, firstname=firstName)
    if employee is None:
        raise HTTPException(status_code=404, detail="employee not found")
    return employee


@router.get("/employees/", response_model=List[EmployeeDetailsModel])
def get_employees(
        skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    employees = employee_service.get_employees(session=session, skip=skip, limit=limit)
    return [i for i in employees]


@router.post(
    "/employees/",
    response_model=EmployeeDetailsModel
)
def create_employee(employee: EmployeeBase, session: Session = Depends(get_session)):
    db_employee = employee_service.get_employee_by_email(session, email=employee.email)
    if db_employee:
        raise HTTPException(status_code=400, detail="Employee already created")
    else:
        return employee_service.create_employee(session=session, employee=employee)


@router.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: int, session: Session = Depends(get_session)):
    employee_service.delete_employee(session, employee_id)
    return None


@router.put("/employees/{employee_id}", response_model=EmployeeDetailsModel)
def update_employee(employee_id: int, data: EmployeeBase, session: Session = Depends(get_session)):
    employee = employee_service.update_employee(session, employee_id, data)
    if employee is None:
        raise HTTPException(status_code=404)
    return employee
