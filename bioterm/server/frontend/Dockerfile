# develop stage#
FROM node:18.16.1-alpine3.18
WORKDIR /app
RUN apk update && apk add bash

COPY web_ui/package*.json ./
RUN npm i -g @quasar/cli
RUN npm install

COPY web_ui ./
COPY .env ./.env
WORKDIR /app
RUN quasar build -m pwa

# remove pwa mode from the RUN command above during development
# RUN quasar build
