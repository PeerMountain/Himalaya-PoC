#/bin/bash

python manage.py collectstatic --no-input -c

chmod 777 -R /code/static