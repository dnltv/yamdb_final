## YaMDb project

### Description
The YaMDb project collects user reviews (`Review`) of works (`Title`).
The works are divided into categories: "_Books_", "_Films_", "_Music_".
The list of categories (`Category`) can be expanded (for example, you can add a category "*Fine Arts*" or "*Jewelry*").

More information in the base [repository](https://github.com/dnltv/api_yamdb).


### Preparing for launch
- Clone the repository and go to it on the command line.
```bash
git clone https://github.com/dnltv/infra_sp2.git
cd infra_sp2
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
ADJANGO_TOKEN=YOUR_TOKEN
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

### Author:
- [Danil Treskov](https://github.com/dnltv)
