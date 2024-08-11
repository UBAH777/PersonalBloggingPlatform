# PersonalBloggingPlatform API

Проект представляет собой API для создания записей в собственном блоге и управления ими. В основе построения архитектуры лежит REST подход, реализует JSON-API.


### Технологии

- python
- пакеты python из файла requirements.txt
- make

### Структура

```shell
.
├── app
│   ├── api
│   │   ├── __init__.py
│   │   ├── errors.py
│   │   └── routes.py
│   ├── __init__.py
│   ├── models.py
├── migrations
├── Makefile
├── requirements.txt
├── config.py
├── runner.py
└── Volume
    └── myapp.db
```

### Подготовка и запуск

#### Установка

- установить python в вашей ОС
- установить make в вашей ОС
- склонировать репозиторий

#### Запуск

- при первом запуске (для настройки проекта и запуска): запустить `make launch`
- при последующих запусках: `make run`


### Ссылки

- документация flask: https://flask.palletsprojects.com/en/3.0.x/
- документация jinja2: https://jinja.palletsprojects.com/en/3.1.x/

### API

---

- api/articles GET
- api/articles/<int:id> GET
- api/articles POST
- api/articles/<int:id> PUT
- api/articles/<int:id> DELETE