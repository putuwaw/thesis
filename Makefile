TAILWIND_INPUT = ./thesis/static/css/input.css
TAILWIND_OUTPUT = ./thesis/static/css/output.css
PROJECT_DIR = ./thesis

tw-watch:
	@npx tailwindcss -i $(TAILWIND_INPUT) -o $(TAILWIND_OUTPUT) --watch

tw-minify:
	@npx tailwindcss -o $(TAILWIND_OUTPUT) --minify

django-dev:
	@cd thesis && python manage.py runserver

html-reformat:
	@djlint ${PROJECT_DIR} --reformat --quiet

html-minify:
	@find $(PROJECT_DIR) -name '*.html' -exec sh -c 'html-minifier --collapse-whitespace "$$1" -o "$$1"' _ {} \;