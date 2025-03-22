install:
	uv sync

install-all:
	uv sync --all-groups

collectstatic:
	uv run python3 manage.py collectstatic --noinput

migrate:
	make migrations && uv run python3 manage.py migrate

migrations:
	uv run python3 manage.py makemigrations

build:
	./build.sh

start:
	gunicorn task_manager.wsgi

devserver:
	uv run python3 manage.py runserver

test-coverage:
	coverage report -m
	coverage lcov --output-file reports/lcov.info