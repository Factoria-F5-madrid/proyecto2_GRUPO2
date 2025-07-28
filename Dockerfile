FROM python:3.11.13-slim as base

WORKDIR /app

RUN apt-get update && apt-get install -y bash && \
    rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt


EXPOSE 8000

#CMD python3 myproject/manage.py runserver 0.0.0.0:8000
