# Pull base image
FROM python:3.7

# set environment variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip && pip install pipenv && pipenv install --system

# Copy project
COPY . /code/