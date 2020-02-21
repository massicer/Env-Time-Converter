CHANGELOG ?= CHANGELOG.md
SERVICE_VERSION = `cat pyproject.toml | grep "^version =" | cut -f 3 -d ' ' | cut -d '"' -f 2`

install:
	@echo 'installing all dependencies (also the dev ones)'
	poetry install

test: install ## run all tests
	poetry run pytest -vv --cov=src --cov-report term-missing

codecov-test: install ## run all tests
	poetry run pytest -vv --cov=src  --cov=codecov 

lint: ## lint code
	poetry run flake8 src tests

bump:
	poetry version $(INCREMENT)
	
changelog:
	git-chglog -o $(CHANGELOG) -next-tag $(SERVICE_VERSION)
	
release: test
	$(MAKE) bump INCREMENT=$(INCREMENT)
	$(MAKE) changelog
	git add . && git commit -m "Bump to v$(SERVICE_VERSION)" && git tag -a "v$(SERVICE_VERSION)" -m $(SERVICE_VERSION)

major: ## release a new major
	$(MAKE) release INCREMENT='major'

minor: ## release a new minor
	$(MAKE) release INCREMENT='minor'

patch: ## release a new patch
	$(MAKE) release INCREMENT='patch'
