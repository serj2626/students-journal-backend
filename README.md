# API для проекта "Электронный журнал студентов"

## Требования

- Python 3.12

## Скачать

```bash
git clone https://github.com/serj2626/students-journal-backend
```

## Перейти в директорию

```bash
cd students-journal-backend
```

## Создать файл .env и внести в него данные 

```bash
SECRET_KEY=любой текст без пробелов
```

## Команды для запуска 

<details>

  <summary>Для ubuntu</summary>

    python3.12 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

</details>

<details>

  <summary>Для windows</summary>

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

</details>

---


## Документация

[Swagger](http://127.0.0.1:8000/api/schema/swagger/)
