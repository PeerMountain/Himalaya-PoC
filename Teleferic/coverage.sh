#!/bin/bash
rm htmlcov -Rf
coverage run --source='.' manage.py test
coverage html 