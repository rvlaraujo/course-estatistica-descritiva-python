# syntax = docker/dockerfile:1

FROM python:3.8.18-slim-bullseye

WORKDIR /app

RUN apt-get --force-yes update \
    && apt-get --assume-yes install r-base-core

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . .