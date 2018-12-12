FROM python:3.7-alpine

WORKDIR /app

COPY Pipfile* ./
RUN apk update \
    && apk add --virtual build-deps gcc git python3-dev musl-dev linux-headers pcre-dev \
    && apk add postgresql-dev \
    && pip install --no-cache-dir pipenv \
    && pipenv install --system --deploy \
    && apk del build-deps

COPY . /app
