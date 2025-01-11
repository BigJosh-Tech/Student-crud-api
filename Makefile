run:
	python app.py

migrate:
	flask db migrate -m "Create Student table"

upgrade:
	flask db upgrade

test:
	pytest
