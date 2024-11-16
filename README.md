# thesis

Web-Based Balinese Language Text Classification using MNB

## Prerequisites

This project is basically a Django app with Tailwind CSS, so you need:
- Python 3.10
- npm

But you can easily take a look into the project using Docker, so you need:
- Docker
- docker-compose

## Installation

1. Clone the repository
```
git clone https://github.com/putuwaw/thesis.git
```
2. Pull the submodules (thesis-ml). Note that submodules here are using SSH, learn more about setup SSH for GitHub [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh):
```
git submodules update --init
```
3. Create env file and change the content especially database.
```
cp .env.example .env.development
```

4. Using Django and Tailwind CSS:

Setup environment and install packages
```
python -m venv .venv
source .venv/bin/activate
pip install -r thesis/requirements.txt
```

Run Django and watch tailwind:
```bash
make django-dev
make tw-watch
```
5. You can also use Docker:

If you are using Docker, you don't need to change the Django database env.
Run docker container, migrate database, collect static files:
```
docker compose -f compose.dev.yml up -d --build
docker compose -f compose.dev.yml exec web python manage.py migrate --noinput
docker compose -f compose.dev.yml exec web python manage.py collectstatic --noinput
```

### Production:

- Run all the services:
```bash
docker compose up -d --build
```
- Run database migration, and serve static files:
```bash
docker compose exec web python manage.py migrate  --noinput
docker compose exec web python manage.py collectstatic  --noinput
```
- Create super admin user:
```bash
docker compose exec web python manage.py createsuperuser
```