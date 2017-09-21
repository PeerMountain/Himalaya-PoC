FROM python:3.5.2

MAINTAINER DXMarkets

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/

RUN python manage.py collectstatic --clear --noinput

EXPOSE 8000

ENV PRODUCTION 1

CMD ./run.sh