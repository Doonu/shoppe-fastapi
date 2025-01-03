Создание сессий:
https://gist.github.com/zmts/802dc9c3510d79fd40f9dc38a12bccfc

Запуск приложения:
1) dev сборка - ```./run.sh```
2) prod сборка - ```./run.sh prod```

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
 В ходе установки добавлены следующие пакеты:
- FastAPI и его основные зависимости: Starlette и Pydantic, которые обеспечивают маршрутизацию, обработку запросов и валидацию данных.
- Дополнительные пакеты для FastAPI: FastAPI-CLI для командной строки, HTTPX для выполнения HTTP-запросов, Jinja2 для шаблонов HTML, Python-multipart для обработки файловых загрузок, и Uvicorn для запуска сервера ASGI.
- Поддержка различных форматов данных и безопасности: PyYAML, UJSON, Orjson, и Email-validator.
- Дополнительные пакеты для улучшения работы и разработки: Pydantic-settings и Pydantic-extra-types для расширенной конфигурации и типов, Typer для работы с CLI, а также Rich для вывода в консоль._

----
Контроль версий `poetry`
----
1. ``` poetry init```
2. Синхронизация между окружением и системой контроля зависимостей
```poetry install --sync```

----
Использование базы данных Postgres + Docker
----
- ```docker pull postgres```

Создание базы данных с именем todo-db и паролем - qwerty, порта для использования 5436
После остановки контейнера - он удаляется 
- ```docker run --name=shopp_db -e POSTGRES_PASSWORD="qwerty" -p 5436:5432 -d --rm postgres```

Подключение к базе данных
- ```docker ps``` (вытаскиваем id контейнер)
- ```docker exec -it <id Container> /bin/bash``` (запускаем контейнер)
- ```psql -U postgres```
- ```\d```

-----------------------
Миграции баз данных
-----------------------

Иницализация миграции
- ```alembic init migrations```

Создание ревизии
- ```alembic revision --autogenerate -m "Database creation"```

Повышение
- ```alembic upgrade <hash из verions в переменной revision (head)>``` 

----------------------
Документация
----------------------

Описание зависимостей:
- ```FastAPI```: Основной фреймворк для создания API-приложений. В версии ^0.115.2 ты получаешь актуальные возможности по работе с асинхронностью,
роутингом, валидацией данных через Pydantic и др.

- ```Uvicorn```: Асинхронный сервер для запуска FastAPI. Ты используешь версию с extras=["standard"],
что добавляет поддержку таких возможностей, как websockets и интеграция с различными протоколами.

- ```SQLAlchemy```: ORM для работы с базами данных. Ты указал extras=["asynio"],
чтобы использовать асинхронные функции взаимодействия с базой данных.

- ```Asyncpg```: Асинхронный драйвер для PostgreSQL. Он нужен для того, чтобы взаимодействовать с
базой данных PostgreSQL через асинхронные вызовы.

- ```Pydantic-settings```: Инструмент для управления конфигурацией через Pydantic,
что позволяет удобно работать с настройками приложения.

- ```Alembic```: Утилита для миграций базы данных. Она используется для управления схемой базы данных и выполнения версионирования.
Для разработки:
- ```Pytest```: Фреймворк для тестирования. Версия ^8.3.3 позволит тебе писать юнит-тесты и обеспечивать качество кода.
- ```Black```: Инструмент для автоформатирования Python-кода, чтобы поддерживать единый стиль в проекте.

Описание модулей и файлов:

CORE:
- config.py - Используется pydentic для управлния конфигурацией приложения через класс Settings
1) api_v1_prefix: Префикс для версий API, по умолчанию /api/v1.
2) db_url: URL для подключения к базе данных, использующий драйвер PostgreSQL и библиотеку asyncpg.
3) echo: Параметр для логирования запросов в базу данных. Полезен для отладки, когда установлен в True.

- base.py - Содержит базовый класс для моделей баз данных с использованием SQLAlchemy.
1) Класс Base: Определен как абстрактный класс с автоматическим определением имени
таблицы через метод __tablename__. Атрибут id используется как первичный ключ.


- db_helper.py (помощник для работы с базой данных) - в этом файле используется SQLAlchemy для асинхронного
использования базы данных
1) DatabaseHelper: Класс для управления подключением к базе данных. Он инициализирует асинхронный движок с помощью create_async_engine
и создает сессии для работы с базой данных.
2) create_async_engine - Метод для создания асинхронного движка базы данных
3) async_sessionmaker - Создание фабрики
4) get_scoped_session - Создание сессии с областью видимости (async_scoped_session)


`Фабрика сессий` в `SQLAlchemy` — это способ стандартизировать создание сессий для работы с 
базой данных. Она позволяет легко управлять жизненным циклом сессий, гарантируя, 
что каждая сессия будет иметь правильную конфигурацию и привязку к нужному движку 
(или базе данных).

```python
self.session_factory = async_sessionmaker(  
    bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False  
)  # Создание фабрики для создания сессий через sessionmaker
```

- `bind`=self.engine:   
    Этот параметр связывает фабрику с конкретным асинхронным движком базы данных, который был создан через create_async_engine. Это значит, что все сессии, созданные через эту фабрику, будут взаимодействовать с этой базой данных
    
- `autoflush`=False:  
    Когда autoflush=True, SQLAlchemy автоматически отправляет изменения в базу данных перед выполнением любого SQL-запроса, если объект был изменён. Ты отключил это поведение, чтобы вручную управлять тем, когда данные должны быть отправлены в базу (например, при вызове session.commit()). Это полезно для оптимизации производительности, так как ты можешь избежать ненужной отправки данных.
    
- `autocommit`=False:  
    Когда autocommit=True, SQLAlchemy будет автоматически завершать транзакции без необходимости явного вызова commit(). В твоем случае, ты отключил это поведение, что даёт тебе полный контроль над транзакциями. Ты должен вручную вызывать commit(), когда хочешь сохранить изменения, или rollback(), если нужно отменить транзакции.
    
- `expire_on_commit`=False:  
    Обычно, когда вызывается session.commit(), все объекты в сессии становятся "недействительными" (их данные будут считаны снова из базы данных при следующем обращении). Установив этот параметр в False, ты оставляешь объекты "актуальными" после коммита, что может быть полезно, если ты не хочешь, чтобы данные пересчитывались сразу после сохранения.

### Как работает фабрика?
`Создание сессии`:  
  
Каждый раз, когда ты вызываешь self.session_factory(), фабрика создаёт новую сессию, привязанную к текущему движку (базе данных). Это асинхронная сессия, которая может использоваться в асинхронных функциях для выполнения запросов к базе данных.  

`Использование сессии`:  
  
- Эта сессия предоставляет все возможности SQLAlchemy для управления транзакциями, запросами и обновлениями данных.  
- Ты можешь использовать методы сессии, такие как add(), delete(), commit(), rollback(), и выполнять запросы к базе данных.  

`Управление сессиями в FastAP`I:  
  
В контексте FastAPI ты используешь эту фабрику для создания сессий, которые могут быть переданы в эндпоинты через зависимости. Например, ты можешь передавать сессию в функции с помощью Depends
```python
async def get_items(db: AsyncSession = Depends(db_helper.session_dependency)):  
	result = await db.execute("SELECT * FROM items")  
	items = result.fetchall()  
	return items
```


### Жизненный цикл сессии:  
`Создание сессии`:  
Когда функция FastAPI вызывает зависимость session_dependency, фабрика создаёт новую сессию, которая будет использоваться для обработки текущего запроса. 

`Выполнение запросов`:  
Во время запроса сессия выполняет взаимодействие с базой данных (вставки, обновления, выборки и т.д.).  

`Завершение запроса`:  
Когда запрос завершён, FastAPI завершает работу сессией (либо коммитом, если все прошло успешно, либо откатом транзакции, если возникла ошибка).  
После завершения запроса сессия закрывается, и все ресурсы освобождаются.

### Методы
`add`(): Используется для добавления одного объекта в сессию.  
`add_all`(): Используется для добавления нескольких объектов в сессию.  
`commit`(): Фиксирует все изменения, сделанные в сессии, сохраняя их в базе данных.  
`rollback`(): Откатывает все изменения в текущей транзакции.  
`close`(): Закрывает сессию, освобождая ресурсы.  
`delete`(): Удаляет объект из базы данных.  
`flush`(): Отправляет изменения в базу данных без завершения транзакции.  
`expire`(): Помечает объект для обновления его данных при следующем обращении.  
`refresh`(): Принудительно обновляет данные объекта из базы данных.  
`execute`() и scalar(): Выполняет запрос и возвращает одно значение из результата.  
`scalars`(): Возвращает несколько объектов из результата запроса.  
`get`(): Возвращает объект по его первичному ключу.  
`merge`(): Объединяет изменения объекта с объектом в текущей сессии.

------------------------------
Связи между таблицами
------------------------------

shared:
Используется mixin для обращение к таблице user (обернуть в этот класс и получить привязку к этой таблице)
```
class UserRelationMixin:
    _user_id_unique: bool = False
    _user_back_populates: Optional[str] = None
    _user_id_nullable: bool = False

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("user.id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable,
        )

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship("User", back_populates=cls._user_back_populates)
```

1) Один ко многим
Отношение «один ко многим» (One-to-Many) между таблицами в базе данных означает, что 
одна запись в одной таблице может быть связана с несколькими записями в другой таблице. 
Например, один пользователь может иметь несколько постов - User и Post.

user.py
```
    posts: Mapped[list["Post"]] = relationship(back_populates="user")
```

2) Один к одному
Связь «один к одному» (One-to-One) в базе данных означает, что каждая запись в одной таблице может быть связана 
только с одной записью в другой таблице. Это полезно, когда ты хочешь разделить данные между двумя таблицами, но 
поддерживать уникальное соответствие между записями.
user.py и profile.py

user.py
```
profile: Mapped["Profile"] = relationship(back_populates="user")
```
