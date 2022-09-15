FROM python:3.10
WORKDIR /employee
COPY . /employee
RUN pip install -r requirements.txt
ENTRYPOINT ["./docker-entrypoint.sh"]