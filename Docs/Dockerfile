FROM node:boron

RUN mkdir -p /code
WORKDIR /code

RUN npm install -g @2fd/graphdoc

ADD build_docs.sh .

CMD ./build_docs.sh