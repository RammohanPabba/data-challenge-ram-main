default: run

.PHONY: install
install:
	pip install poetry
	poetry install

.PHONY: start-db
start-db:
	docker-compose up

.PHONY: run
run:
	docker-compose up && \
	poetry run python ./data_extractor/main.py

.PHONY: lint
lint:
	poetry run black .

.PHONY: test
test:
	poetry run pytest

.PHONY: generate-data
generate-data:
	poetry run python ./scripts/generate_data.py
