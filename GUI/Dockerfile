FROM node:boron
RUN mkdir -p /code
WORKDIR /code
COPY package.json /code
RUN npm install
COPY . /code
EXPOSE 3000
RUN ["npm", "run", "build"]
CMD ["npm", "run", "serve"]