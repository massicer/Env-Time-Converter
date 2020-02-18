install:
	@echo 'installing all dependencies (also the dev ones)'
	poetry install

test: ## run all tests
	poetry run pytest -vv --cov=src --cov-report term-missing

lint: ## lint code
	poetry run flake8 src tests