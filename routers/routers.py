from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import SessionLocal, engine
from models import employee
from schemas.schemas import EmployeeDetailsModel, EmployeeBase
from utils import crud

employee.Base.metadata.create_all(bind=engine)
router = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@router.get("/employees/{firstName}", response_model=EmployeeDetailsModel)
def find_employee_by_firstname(firstName: str, session: Session = Depends(get_session)):
    employee = crud.get_employee_by_firstname(session=session, firstName=firstName)
    if employee is None:
        raise HTTPException(status_code=404, detail="employee not found")
    return employee.serialize


@router.get("/employees/", response_model=List[EmployeeDetailsModel])
def get_employees(
        skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    employees = crud.get_employees(session=session, skip=skip, limit=limit)
    return [i.serialize for i in employees]
