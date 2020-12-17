
FROM python: 3.7.3

# set work directory
WORKDIR /backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /backend
RUN pip install -r requirements.txt

# copy project
COPY . /backend/

# migrate
RUN python manage.py migrate