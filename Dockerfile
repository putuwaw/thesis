FROM python:3.10-slim

# prevent .pyc files, -B
ENV PYTHONDONTWRITEBYTECODE 1
# prevent buffering, -u
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# psycopg2 need libpq-dev and gcc
RUN apt-get update && apt-get install -y libpq-dev gcc

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# copy all files
COPY . .

# install dependencies using uv
RUN uv sync --frozen

WORKDIR /app/thesis

# config file by default: ./gunicorn.conf.py
CMD [ "uv", "run", "gunicorn", "thesis.wsgi:application" ]
