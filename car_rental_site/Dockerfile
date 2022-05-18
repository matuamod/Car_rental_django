FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /django_app/car_rental_site

COPY ./requirements.txt /django_app/requirements.txt
RUN pip install -r /django_app/requirements.txt

COPY . /django_app/car_rental_site

RUN ["chmod", "+x", "/django_app/car_rental_site/manage.py"]

