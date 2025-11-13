all: clean build


deploy: clean install staticsite


install:
	pip install uv
	uv sync


staticsite:
	mkdir -p docs
	mkdir -p django-staticsite-example/static
	uv run django-staticsite-example/manage.py collectstatic --noinput
	uv run django-staticsite-example/manage.py staticsite generate --output-directory=docs --force --quiet


clean:
	rm -rf docs
	rm -rf django-staticsite-example/static
