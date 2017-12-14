#/bin/bash

if [ ! -f ./.env ]
then
  virtualenv -p python3 .env
fi

. .env/bin/activate
pip install -r requirements.txt

python manage.py collectstatic -c --noinpu