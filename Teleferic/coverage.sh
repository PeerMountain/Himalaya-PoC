#/bin/bash

if [ ! -f ./.env ]
then
  virtualenv -p python3 .env
fi

. .env/bin/activate
pip install -r requirements.txt

if [ ! -f ./htmlcov ]
then
  rm htmlcov -Rf
fi

DEBUG=1 coverage run --source='.' manage.py test

coverage html 