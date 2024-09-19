# thesis

Web-Based Balinese Language Text Classification using MNB

## Prerequisites

This project is basically a Django app with Tailwind CSS, so you need:
- Python 3.10
- npm

But you can easily take a loot into the project using Docker, so you need:
- Docker
- docker-compose

## Installation

Development:
```bash
make run-dev
```

Production:
- Run all the services:
```bash
docker-compose up -d --build
```
- Run database migration, and serve static files:
```bash
docker-compose exec web python manage.py migrate  --noinput
docker-compose exec web python manage.py collectstatic  --noinput
```
- Create super admin user:
```bash
docker-compose exec web python manage.py createsuperuser
```