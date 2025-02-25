run:
	python app.py

migrate:
	flask db migrate -m "Create Student table"

upgrade:
	flask db upgrade

test:
	pytest

# Variables
VERSION=1.0.0
IMAGE_NAME=student-crud-api
DOCKER_USER=mydockerhubuser
DOCKER_REPO=mydockerhubrepo

.PHONY: install test lint build docker-login docker-build docker-push

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/

lint:
	python -m flake8 --exclude=venv . 

build:
	docker build -t $(IMAGE_NAME):$(VERSION) .

docker-login:
	echo "$(DOCKER_PASSWORD)" | docker login -u "$(DOCKER_USERNAME)" --password-stdin

docker-build:
	docker build -t $(DOCKER_USER)/$(DOCKER_REPO):$(VERSION) .

docker-push: docker-build
	docker push bigjosh03/mydockerhubrepo:1.0.0
