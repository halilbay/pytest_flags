# Makefile for managing Docker Compose and running pytest with various flags

# Docker Compose command
DOCKER_COMPOSE=docker compose

# Poetry run command inside Docker container
DOCKER_EXEC=$(DOCKER_COMPOSE) run --rm app poetry run pytest --disable-warnings

# Default target to build and start the Docker Compose environment
up:
	$(DOCKER_COMPOSE) run --rm app

# Stop all running containers
stop:
	$(DOCKER_COMPOSE) down

# Show pytest commands
help:
	$(DOCKER_EXEC) --help

# Run all tests inside the Docker container
test:
	$(DOCKER_EXEC)

# Run tests matching a keyword inside the Docker container
test-keyword:
	$(DOCKER_EXEC) -k "$(keyword)"

# Run tests excluding a keyword inside the Docker container
test-exclude-keyword:
	$(DOCKER_EXEC) -k "not $(keyword)"

# Show markers the Docker container
test-show-marker:
	$(DOCKER_EXEC) --markers

# Run tests with a specific marker inside the Docker container
test-marker:
	$(DOCKER_EXEC) -m "$(marker)"

# Run tests and generate coverage report inside the Docker container
test-coverage:
	$(DOCKER_EXEC) --cov=app --cov-report=term-missing  --cov-fail-under=80

# Run tests with detailed output for debugging inside the Docker container
test-debug:
	$(DOCKER_EXEC) -s -v

# Run tests with detailed output for debugging inside the Docker container
test-debug-alternative:
	$(DOCKER_EXEC) -s -v --pdb

# Run parameterized tests specifically inside the Docker container
test-parametrize:
	$(DOCKER_EXEC) -m "parametrize"

# Run tests with a specific test file or directory inside the Docker container
test-file:
	$(DOCKER_EXEC) $(file)


# Run tests with a custom flag inside the Docker container
test-custom:
	$(DOCKER_EXEC) "${flag}"



.PHONY: up stop test test-keyword test-exclude-keyword test-marker test-coverage test-debug test-parametrize test-file
