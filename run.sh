#!/bin/bash

set -e

docker-compose up -d db || { echo "Ошибка при запуске docker-compose"; exit 1; }

alembic upgrade head || { echo "Ошибка при применении миграций"; exit 1; }

cleanup() {
  echo "Остановка контейнеров..."
  docker-compose down db
}

trap cleanup EXIT

uvicorn main:app --host localhost --port 8000 || { echo "Ошибка при запуске Uvicorn"; exit 1; }