install:
	uv sync

collectstatic:
	uv run python3 manage.py collectstatic

migrate:
	make migrations && uv run python3 manage.py migrate

migrations:
	uv run python3 manage.py makemigrations

build:
	./build.sh

shell:
	source .venv/bin/activate

render-start:
	uv run gunicorn task_manager.wsgi