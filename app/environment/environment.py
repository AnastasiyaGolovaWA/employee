from os import environ

DB_USER = environ.get("DB_USER", "postgres")
DB_PASSWORD = environ.get("DB_PASSWORD", "root")
DB_HOST = environ.get("DB_HOST", "127.0.0.1")
DB_NAME = environ.get("DB_NAME", "employees")
DB_PORT = environ.get("DB_PORT", "5437")
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(DB_URL)