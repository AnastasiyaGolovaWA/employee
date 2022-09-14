from typing import List

from sqlalchemy.orm import Session
from typing import Union
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


def delete_employee(session: Session, employee_id: int):
    session.query(Employee).filter(Employee.id == employee_id).delete()
    session.commit()
    return None


def get_employee(session: Session, id: int):
    return session.query(Employee).get(id)


def update_employee(session: Session, employee: Union[int, Employee], data: EmployeeBase):
    if isinstance(employee, int):
        employee = get_employee(session, employee)
    if employee is None:
        return None
    for key, value in data:
        setattr(employee, key, value)
    session.commit()
    return employee
