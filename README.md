# backend_shoppe

Настроить виртуальное окружения в PyCharm (File --> Python Interpretator)

1. Создание виртуального окружения
```python -m venv venv```
2. Активация вирутального окружения
```.\venv\Scripts\activate```
3. Установка зависимостей
```
   pip install fastapi[all] 
   pip install sqlalchemy alembic psycopg2
```
4. Сохрнанение зависимостей
```
 pip freeze > reaquirements.txt
```

 В ходе установки добавлены следующие пакеты:
- FastAPI и его основные зависимости: Starlette и Pydantic, которые обеспечивают маршрутизацию, обработку запросов и валидацию данных.
- Дополнительные пакеты для FastAPI: FastAPI-CLI для командной строки, HTTPX для выполнения HTTP-запросов, Jinja2 для шаблонов HTML, Python-multipart для обработки файловых загрузок, и Uvicorn для запуска сервера ASGI.
- Поддержка различных форматов данных и безопасности: PyYAML, UJSON, Orjson, и Email-validator.
- Дополнительные пакеты для улучшения работы и разработки: Pydantic-settings и Pydantic-extra-types для расширенной конфигурации и типов, Typer для работы с CLI, а также Rich для вывода в консоль.

----
Контроль версий `poetry`
----
1. 
```
    poetry init
```
2. Синхронизация между окружением и системой контроля зависимостей
```
   poetry install --sync
```

----
Использование базы данных Postgres + Docker
----
- ***docker pull postgres***

Создание базы данных с именем todo-db и паролем - qwerty, порта для использования 5436
После остановки контейнера - он удаляется 
- ***docker run --name=shopp_db -e POSTGRES_PASSWORD="qwerty" -p 5436:5432 -d --rm postgres***

Подключение к базе данных
- docker ps (вытаскиваем id контейнер)
- docker exec -it <id Container> /bin/bash
- psql -U postgres
- \d

-----------------------
Миграции баз данных
-----------------------

Иницализация миграции
- alembic init migrations

Создание ревизии
- alembic revision --autogenerate -m "Database creation"

Повышение
- alembic upgrade <hash из verions в переменной revision> 