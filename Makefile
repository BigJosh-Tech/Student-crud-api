run:
	python app.py

migrate:
	flask db migrate -m "Create Student table"

upgrade:
	flask db upgrade

test:
	pytest

# Define variables
IMAGE_NAME = student-crud-api
TAG = 1.0.0
DB_URL ?= sqlite:///students.db

.PHONY: build run stop

build:
	docker build -t student-crud-api:1.0.0 .

run:
	docker run -d -p 5000:5000 --env-file .env student-crud-api:1.0.0 

stop:
	@docker ps | grep $(IMAGE_NAME):$(VERSION) | awk '{print $$1}' | xargs docker stop
