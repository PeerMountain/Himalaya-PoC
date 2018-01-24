FROM python:3.5.2

MAINTAINER DXMarkets

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

RUN apt update
RUN apt install zip postgresql-client -y

ADD gunicorn_conf.py /code/
ADD manage.py /code/
ADD run.sh /code/
ADD settings.py /code/
ADD libs /code/libs
ADD Teleferic /code/Teleferic
ADD API /code/API

ADD coverage.sh /code/

ADD reset.sh /code/

EXPOSE 8000

ENV PRODUCTION 1

CMD ./run.sh
