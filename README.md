[![Django-app workflow](https://github.com/dnltv/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/dnltv/yamdb_final/actions/workflows/yamdb_workflow.yml)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=5381ff&color=830f00)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=5381ff&color=830f00)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=830f00)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=5381ff&color=830f00)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=830f00)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=5381ff&color=830f00)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=5381ff&color=830f00)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=5381ff&color=830f00)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=5381ff&color=830f00)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=5381ff&color=830f00)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=5381ff&color=830f00)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=5381ff&color=830f00)](https://cloud.yandex.ru/)
## YaMDb project

### Description
The YaMDb project collects user reviews (`Review`) of works (`Title`).
The works are divided into categories: "_Books_", "_Films_", "_Music_".
The list of categories (`Category`) can be expanded (for example, you can add a category "*Fine Arts*" or "*Jewelry*").

More information in the base [repository](https://github.com/dnltv/api_yamdb).


### Preparing for launch
- Clone the repository and go to it on the command line.
```bash
git clone https://github.com/dnltv/yamdb_final.git
cd yamdb_final
```

- Install and activate the virtual environment taking into account the Python 3.7 version (choose python at least 3.7):

For Linux / MacOS:
```bash
python3.7 -m venv venv
```

```bash
. venv/bin/activate
```

For Windows:
```bash
py -3.7 -m venv venv
```

```bash
source venv/Scripts/activate
```

- Install all dependencies from the file **requirements.txt**

```bash
python -m pip install --upgrade pip
pip install -r api_yamdb/requirements.txt
```

#### Environment variables
- Create `.env` file in the `infra` directory according to the following pattern
```bash
nano infra/.env
```

```
DJANGO_TOKEN=YOUR_TOKEN
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=YOUR_PASSWORD
DB_HOST=db
DB_PORT=5432
```

### Launch project

- Build docker-compose
```bash
cd infra
docker-compose up -d --build
```

- Perform migrations:
```bash
docker-compose exec web python manage.py migrate
```

- Create a `superuser`:
```bash
docker-compose exec web python manage.py createsuperuser
```

- Collect project static:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

- If necessary, fill in the database with test data with the command:
```bash
docker-compose exec web python manage.py loaddata fixtures.json
```

- Stop containers:
```bash
docker-compose down -v
```

Workflow

tests - Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest. Дальнейшие шаги выполнятся только если push был в ветку master или main.
build_and_push_to_docker_hub - Сборка и доставка докер-образов на Docker Hub
deploy - Автоматический деплой проекта на боевой сервер. Выполняется копирование файлов из репозитория на сервер:
send_message - Отправка уведомления в Telegram

### Author:
- [Danil Treskov](https://github.com/dnltv)
