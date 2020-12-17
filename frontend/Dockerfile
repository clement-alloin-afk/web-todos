# set work directory
WORKDIR /frontend

COPY package.json ./
COPY package-lock.json ./

RUN npm install

COPY . /frontend/

RUN npm run build