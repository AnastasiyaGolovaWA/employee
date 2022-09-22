from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from app import services
from app.database.database import SQLALCHEMY_DATABASE_URI
from app.main import app
from app.routers.routers import get_session
from app.services import crud

engine = create_engine(SQLALCHEMY_DATABASE_URI)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
client = TestClient(app)


def override_get_session():
    try:
        session = TestingSessionLocal()
        yield session
    finally:
        session.close()


app.dependency_overrides[get_session] = override_get_session


def test_endpoints():
    response_create = client.post("/employees/", json={
        "firstName": "firstName",
        "lastName": "lastName",
        "email": "testtest@gmail.com",
        "experience": 5
    })
    obj = response_create.json()
    assert response_create.status_code == 200

    response_update = client.put(f"/employees/{obj['id']}", json={
        "firstName": "firstName",
        "lastName": "lastName",
        "email": "test@gmail.com",
        "experience": 10
    })

    assert response_update.status_code == 200

    response_delete = client.delete(f"/employees/{obj['id']}")

    assert response_delete.status_code == 204


def test_valid_firstname():
    response = client.get("/employees/nastya")
    assert response.status_code == 200
    assert response.json() == {
        "firstName": "nastya",
        "lastName": "golova",
        "email": "tesemail",
        "experience": 0,
        "id": 8
    }


def test_invalid_firstname():
    response = client.get("/employees/invalid")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "employee not found"
    }


def test_endpoints_with_default_values():
    response_create = client.post("/employees/", json={
        "email": "testtest@gmail.com"
    })
    obj = response_create.json()
    assert response_create.status_code == 200

    response_update = client.put(f"/employees/{obj['id']}", json={
        "firstName": "firstNameUpdateTest",
        "lastName": "lastNameUpdateTest",
        "email": "test@gmail.com",
        "experience": 10
    })

    assert response_update.status_code == 200

    response_delete = client.delete(f"/employees/{obj['id']}")

    assert response_delete.status_code == 204


def test_find_employee_by_firstname():
    db = next(override_get_session())
    result = services.crud.get_employee_by_firstname(db, "nastya")
    assert result.firstName == "nastya"
