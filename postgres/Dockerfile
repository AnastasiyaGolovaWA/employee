FROM python:3.10
WORKDIR /employee
COPY .. /employee
RUN pip install --no-cache-dir --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi
ENTRYPOINT ["./postgres/docker-entrypoint.sh"]