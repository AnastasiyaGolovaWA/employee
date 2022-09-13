from sqlalchemy import desc, select

from models.database import database
from models.employee import employees_table
from schemas import employee as employee_schema


async def create_employee(employee: employee_schema.EmployeeModel):
    query = (
        employees_table.insert()
        .values(
            firstName=employee.firstName,
            lastName=employee.lastName,
            email=employee.email,
            experience=employee.experience,
        )
        .returning(
            employees_table.c.id,
            employees_table.c.firstName,
            employees_table.c.lastName,
            employees_table.c.email,
            employees_table.c.experience,
        )
    )
    employee = await database.fetch_one(query)

    employee = dict(zip(employee, employee.values()))
    return employee


async def get_employee(employee_id: int):
    query = (
        select(
            [
                employees_table.c.id,
                employees_table.c.firstName,
                employees_table.c.lastName,
                employees_table.c.email,
                employees_table.c.experience,
            ]
        )
        .select_from(employees_table)
        .where(employees_table.c.id == employee_id)
    )
    return await database.fetch_one(query)


async def get_employees(page: int):
    max_per_page = 10
    offset1 = (page - 1) * max_per_page
    query = (
        select(
            [
                employees_table.c.id,
                employees_table.c.firstName,
                employees_table.c.lastName,
                employees_table.c.email,
                employees_table.c.experience,
            ]
        )
        .select_from(employees_table)
        .order_by(desc(employees_table.c.experience))
        .limit(max_per_page)
        .offset(offset1)
    )
    return await database.fetch_all(query)
