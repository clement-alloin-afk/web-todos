FROM python:3.9-alpine

# set work directory
WORKDIR /backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY requirements.txt /backend
RUN pip install -r requirements.txt

# copy project
COPY . /backend/

ENTRYPOINT ["/backend/entrypoint.sh"]