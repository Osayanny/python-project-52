install:
	uv sync

collectstatic:
	uv run python3 manage.py collectstatic --noinput

migrate:
	make migrations && uv run python3 manage.py migrate

migrations:
	uv run python3 manage.py makemigrations

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

devserver:
	uv run python3 manage.py runserver