from typing import List

from sqlalchemy.orm import Session

from models.employee import Employee
from schemas.schemas import EmployeeBase


def get_employee_by_firstname(session: Session, firstname: str) -> Employee:
    return session.query(Employee).filter(Employee.firstName == firstname).first()


def get_employees(session: Session, skip: int = 0, limit: int = 100) -> List[Employee]:
    return session.query(Employee).offset(skip).limit(limit).all()


def create_employee(session: Session, employee: EmployeeBase):
    db_employee = Employee(firstName=employee.firstName, lastName=employee.lastName,
                           email=employee.email,
                           experience=employee.experience)
    session.add(db_employee)
    session.commit()
    session.refresh(db_employee)
    return db_employee


def get_employee_by_email(session: Session, email: str):
    return session.query(Employee).filter(Employee.email == email).first()
