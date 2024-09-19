TAILWIND_INPUT = ./thesis/static/css/input.css
TAILWIND_OUTPUT = ./thesis/static/css/output.css

tw-watch:
	npx tailwindcss -i $(TAILWIND_INPUT) -o $(TAILWIND_OUTPUT) --watch

tw-minify:
	npx tailwindcss -o $(TAILWIND_OUTPUT) --minify

django-dev:
	cd thesis && python manage.py runserver

run-dev:
	make tw-watch & make django-dev
