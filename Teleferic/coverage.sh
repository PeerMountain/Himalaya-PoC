#/bin/bash

coverage run --source='.'  manage.py test API

coverage html

mkdir -p /code/coverage

mv htmlcov /code/coverage
