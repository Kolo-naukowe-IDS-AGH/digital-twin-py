#!/bin/bash -e
docker-compose -f docker-compose.test.yml build --pull
docker compose -f docker-compose.test.yml run -e --rm tests  pytest .
docker-compose -f docker-compose.test.yml down --remove-orphans
