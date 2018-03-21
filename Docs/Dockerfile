FROM node:boron

RUN mkdir -p /code
WORKDIR /code

RUN npm install -g @2fd/graphdoc

CMD graphdoc -e http://teleferic:8000/teleferic -o ./build --force

CMD chmod 777 -R ./build