FROM python:3.10-slim AS build

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

# multi stage
FROM python:3.10-slim AS runtime
WORKDIR /app

# runtime dependencies, cache
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# copy uv binary
COPY --from=build /bin/uv /bin/uvx /bin/

# copy all files
COPY --from=build /app /app

WORKDIR /app/thesis

# config file by default: ./gunicorn.conf.py
CMD [ "uv", "run", "gunicorn", "thesis.wsgi:application" ]
