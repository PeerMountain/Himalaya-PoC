#!/bin/sh

gunicorn -c gunicorn_conf.py Teleferic.wsgi:application --reload