from typing import List

from sqlalchemy.orm import Session

from models.employee import Employee


def get_employee_by_firstname(session: Session, firstName: str) -> Employee:
    return session.query(Employee).filter(Employee.firstName == firstName).first()


def get_employees(session: Session, skip: int = 0, limit: int = 100) -> List[Employee]:
    return session.query(Employee).offset(skip).limit(limit).all()
