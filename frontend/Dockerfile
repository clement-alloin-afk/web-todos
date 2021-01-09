FROM node:14.4.0-alpine3.10

# set work directory
WORKDIR /frontend

COPY package.json ./
COPY package-lock.json ./

RUN npm install

COPY . /frontend

RUN npm run build