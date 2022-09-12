import sqlalchemy

metadata = sqlalchemy.MetaData()

employees_table = sqlalchemy.Table(
    "employees",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(40), unique=True, index=True),
    sqlalchemy.Column("firstName", sqlalchemy.String(100)),
    sqlalchemy.Column("lastName", sqlalchemy.String(100)),
    sqlalchemy.Column("experience", sqlalchemy.Integer),
)
