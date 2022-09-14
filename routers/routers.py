from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import SessionLocal, engine
from models import employee
from schemas.schemas import EmployeeDetailsModel
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
def read_item(firstName: str, session: Session = Depends(get_session)):
    item = crud.get_employee_by_firstname(session=session, firstName=firstName)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.serialize
