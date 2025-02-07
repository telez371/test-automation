FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* ./

ARG POETRY_GROUP=default
RUN poetry install --no-root --with $POETRY_GROUP

WORKDIR /app

COPY . .

ENV GIT_PYTHON_REFRESH=quiet