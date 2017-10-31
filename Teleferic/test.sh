#!/bin/bash

python manage.py test API --behave_no-skipped --behave_stop  --behave_tags $@