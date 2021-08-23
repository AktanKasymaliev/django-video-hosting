# django-video-hosting
Video hosting based on django and django_channels(for comments)

Hello, in the first, you sould clone rep:
* cloning repository:
```
git clone https://github.com/AktanKasymaliev/django-video-hosting.git
```
* Download virtual enviroment:
```
pip install python3-venv 
Activating: python3 -m venv venv
```
* Install all requirements: 
```
pip install -r requirements.txt
```

* Create a file settings.ini on self project level, copy under text, and add your value: 
```
SECRET_KEY = 
DEBUG = 
DB_PASSWORD = 
DB_USER = 
DB_NAME = 
```

* This project working on Postgresql, so install him:
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib (MacOS) / 
sudo apt-get install postgresql postgresql-contrib (Ubuntu)
sudo -u postgres psql
```
* Enter in your postgresql, and create database:
```
sudo -u postgres psql
CREATE DATABASE <database name>;
CREATE USER <database user> WITH PASSWORD 'your_super_secret_password';
ALTER ROLE <database user> SET client_encoding TO 'utf8';
ALTER ROLE <database user> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <database user> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <database name> TO '<database user>';
```

* Sync database with Django:
```
- python manage.py makemigrations
- python manage.py migrate
```

* Create superuser
```
- python manage.py createsuperuser
```


* And finally start project: `python3 manage.py runserver`
