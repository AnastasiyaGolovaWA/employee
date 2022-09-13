from sqlalchemy.orm import Session

from models.employee import Employee


def get_employee_by_name(session: Session, firstName: str) -> Employee:
    return session.query(Employee).filter(Employee.firstName == firstName).first()
