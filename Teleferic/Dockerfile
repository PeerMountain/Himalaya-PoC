FROM python:3.5.2

MAINTAINER DXMarkets

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD gunicorn_conf.py /code/
ADD manage.py /code/
ADD run.sh /code/
ADD Teleferic /code/Teleferic
ADD settings.py /code/
ADD API /code/API
ADD libs /code/libs

RUN mkdir db

EXPOSE 8000

ENV PRODUCTION 1

RUN python manage.py migrate
RUN python manage.py loaddata genesis_identity.json

CMD ./run.sh