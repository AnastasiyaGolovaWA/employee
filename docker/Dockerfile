FROM python:3.10
WORKDIR /employee
COPY .. /employee

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

ENTRYPOINT ["./docker/docker-entrypoint.sh"]