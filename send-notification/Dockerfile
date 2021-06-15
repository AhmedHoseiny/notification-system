FROM node:14.0.0-alpine

ADD . /usr/src/app

WORKDIR /usr/src/app

RUN npm install

EXPOSE 6000

ENTRYPOINT ["npm", "run", "server"]

