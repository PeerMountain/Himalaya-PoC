#!/bin/sh
python manage.py migrate
gunicorn -c gunicorn_conf.py Teleferic.wsgi:application --reload