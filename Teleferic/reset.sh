#!/bin/bash

./manage.py sqlflush | ./manage.py dbshell
./manage.py migrate
./manage.py loaddata genesis_identity genesis_invite