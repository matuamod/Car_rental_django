FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /car_rental_site

WORKDIR /car_rental_site

COPY . .

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
