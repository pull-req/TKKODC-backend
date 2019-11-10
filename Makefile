.PHONY: build
build:
	docker-compose build

.PHONY: start
start:
	docker-compose up --build

.PHONY: stop
stop:
	docker-compose down

.PHONY: logs
logs:
	docker-compose logs