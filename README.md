# Using Django
A website in Django framework with Google App Engine. 

## Requirements
- [Django version 1.11](https://www.djangoproject.com/)
- [Virtual Env](http://www.virtualenv.org/en/latest/)
- [Compass](http://compass-style.org/install/)

## Database setup
MySQL database is used with this app. secret.py file has to be created
and put in my\_site directory where settings.py is. 

Sample secret.py:

    #DATABASE_ENGINE = 'django.db.backends.sqlite3'
    DATABASE_ENGINE = 'django.db.backends.mysql'
    DATABASE_NAME = 'mysite_db'
    DATABASE_USER = 'user'
    DATABASE_PASS = 'password'

## How to run
- `cd src/sites`
- `virtualenv env`
- `. env/bin/activate`
- `pip install -r requirements.txt`
- `cd my_sites`
- `python manage.py migrate`
- `compass compile`
- `python manage.py runserver`
