#/bin/bash

coverage run --source='.'  manage.py test API --behave_format behave_teamcity:TeamcityFormatter

coverage html

mkdir -p /code/coverage

zip -r /code/coverage/coverage.zip htmlcov/ -j htmlcov -m

rm -R htmlcov
