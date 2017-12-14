#/bin/bash
coverage run --source='.'  manage.py test API --behave_format behave_teamcity:TeamcityFormatter

coverage html

if [ ! -f ./coverage.zip ]
then
  rm coverage.zip
fi

zip -r coverage.zip htmlcov/ -j htmlcov -m

rm -R htmlcov