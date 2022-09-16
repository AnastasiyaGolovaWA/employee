FROM python:3.10
WORKDIR /employee
COPY poetry.lock pyproject.toml ./
RUN pip install --no-cache-dir --upgrade pip
COPY . ./
ENTRYPOINT ["./docker-entrypoint.sh"]