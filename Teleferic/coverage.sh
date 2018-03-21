#/bin/bash

coverage run --source='.'  manage.py test API

coverage html

rm -rf /code/coverage/htmlcov

mv htmlcov /code/coverage/

chmod 777 -R /code/coverage