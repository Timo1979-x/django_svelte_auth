up: docker-up
	docker stats

down:
	docker-compose down

docker-up:
	docker-compose up --build -d

run:
	python manage.py runserver
