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
DOCKER_USER=bigjosh03
DOCKER_REPO=mydockerhubrepo

# Define platform argument dynamically
TARGETPLATFORM ?= linux/amd64

.PHONY: install test lint build docker-login docker-build docker-push

install:
	pip install -r requirements.txt

test:
	pytest

lint:
	python -m flake8 --exclude=venv . 

run:
	python app.py

migrate:
	flask db migrate -m "Create Student table"

upgrade:
	flask db upgrade

build:
	docker build -t $(IMAGE_NAME):$(VERSION) .

docker-login:
	echo "$(DOCKER_PASSWORD)" | docker login -u "$(DOCKER_USERNAME)" --password-stdin

docker-build:
	docker build --build-arg TARGETPLATFORM=$(TARGETPLATFORM) -t $(DOCKER_USER)/$(DOCKER_REPO):$(VERSION) .

docker-push: docker-build
	docker push $(DOCKER_USER)/$(DOCKER_REPO):$(VERSION)
