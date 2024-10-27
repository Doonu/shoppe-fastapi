#!/bin/bash

set -e

docker-compose up -d db || { echo "Ошибка при запуске базы данных"; exit 1; }

current_revision=$(alembic current | grep 'head' || true)

if [ -z "$current_revision" ]; then
  echo "Применение миграций..."
  alembic upgrade head || { echo "Ошибка при применении миграций"; exit 1; }
else
  echo "Миграции не требуются, база данных на последней версии."
fi

cleanup() {
  echo "Остановка контейнеров..."
  docker-compose down db
}

trap cleanup EXIT

uvicorn main:app --host localhost --port 8000 || { echo "Ошибка при запуске Uvicorn"; exit 1; }