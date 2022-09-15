#!/usr/bin/env bash

alembic upgrade head
uvicorn app.main:app --host 127.0.0.1 --port 5438 --reload