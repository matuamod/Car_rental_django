#!/bin/sh

while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

python -m pip install Pillow
python manage.py makemigrations --no-input
python manage.py migrate
python manage.py runserver 0.0.0.0:8000