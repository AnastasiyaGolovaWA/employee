from os import environ

import databases
from fastapi import FastAPI
from sqlalchemy import select

from models.employee import employees_table
from routers import employee

DB_USER = environ.get("DB_USER", "postgres")
DB_PASSWORD = environ.get("DB_PASSWORD", "root")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = "employees"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

    @app.get("/")
    async def read_root():
        query = (
            select(
                [
                    employees_table.c.id,
                    employees_table.c.email,
                    employees_table.c.firstName,
                    employees_table.c.lastName,
                    employees_table.c.experience,
                ]
            )
        )
        return await database.fetch_all(query)


app.include_router(employee.router)
