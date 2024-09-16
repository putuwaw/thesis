FROM python:3.10-slim

# prevent .pyc files, -B
ENV PYTHONDONTWRITEBYTECODE 1
# prevent buffering, -u
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# psycopg2 need libpq-dev and gcc
RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# caching, splitting file and dependencies
COPY . .

# config file by default: ./gunicorn.conf.py
CMD [ "gunicorn", "thesis.wsgi:application" ]
