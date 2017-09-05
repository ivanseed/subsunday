FROM node:boron

WORKDIR /usr/src/app

COPY package.json .

ENV NPM_CONFIG_LOGLEVEL warn

RUN npm install

COPY . .

RUN npm run-script build-css

RUN npm build

EXPOSE 3000