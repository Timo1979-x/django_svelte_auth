up: docker-up
	docker stats

down:
	docker compose down

docker-up:
	docker compose up --build -d

run:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
