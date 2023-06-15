cnf ?= .env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))
RUN_APP = docker exec $(APP_NAME)-front-app-1
RUN_BACK_APP = docker exec $(APP_NAME)-back-app-1

.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

node-install: ## install all dependencies
	$(RUN_APP) npm install

npm-install: ## add new dependency
	$(RUN_APP) npm i $(c)

front-ut: ## run unit test for frontend app
	$(RUN_APP) npm run test

front-e2e: ## run e2e test for frontend app
	$(RUN_APP) npm run e2e

restart-services:  ## restart all services
	docker compose down && docker compose build && docker compose up -d

back-ut:  ## run unit test for backend app
	$(RUN_BACK_APP) coverage run --source=app -m unittest discover -s tests && \
	$(RUN_BACK_APP) coverage report && \
	$(RUN_BACK_APP) coverage html && \
	open ./backend/htmlcov/index.html # mac
	# @xdg-open  ./backend/htmlcov/index.html # linux
