all: clean build


deploy: install build


install:
	pip install uv
	uv sync


build:
	mkdir -p docs
	mkdir -p django-staticsite-example/static
	uv run django-staticsite-example/manage.py collectstatic --noinput
	uv run django-staticsite-example/manage.py staticsite generate --output-directory=docs --force --quiet


clean:
	rm -rf docs
	rm -rf django-staticsite-example/static
