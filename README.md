# thesis

Web-Based Balinese Language Text Classification using MNB.

## Prerequisites

This project is basically a Django app with Tailwind CSS, so you need:
- Python 3.10
- uv
- npm

You can easily take a look into the project using Docker, so optionally you need:
- Docker
- docker-compose

## Installation

1. Clone the repository:
```
git clone https://github.com/putuwaw/thesis.git
```
2. Pull the submodules (thesis-ml). Note that submodules here are using SSH, learn more about setup SSH for GitHub [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh):
```
git submodules update --init
```
3. Create development env file and change the variable especially for database:
```
cp .env.example .env.development
```

4. Using Django and Tailwind CSS:

Setup environment and install packages
```
uv sync --dev
```

Run Django and watch Tailwind:
```bash
make django-dev
make tw-watch
```

5. You can also use Docker:

If you are using Docker, you don't need to create env.
Run Docker container, migrate database, collect static files:
```
docker compose -f compose.dev.yml up -d --build
docker compose -f compose.dev.yml exec web python manage.py migrate --noinput
docker compose -f compose.dev.yml exec web python manage.py collectstatic --noinput
```

## Acknowledgments
I would like to express my deepest gratitude to all those who have supported and contributed to the completion of this thesis.

- Mr. Cokorda Pramartha as my supervisor, for his guidance and support.
- Balinese language counselor for assisting with data annotation.
- Family, partner, and friends for their encouragement and motivation.
