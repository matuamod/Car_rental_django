FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/car_rental

COPY ./requirements.txt /app/car_rental/requirements.txt

RUN pip3 install --upgrade pip

RUN \
    apk update && \
	apk add --no-cache mariadb-connector-c-dev && \
	apk add python3 python3-dev mariadb-dev build-base && \
	pip3 install mysqlclient && \
	apk del python3-dev mariadb-dev build-base

RUN apk add netcat-openbsd

RUN pip install -r /app/car_rental/requirements.txt

# install pillow dependencies
RUN apk add --no-cache jpeg-dev zlib-dev \
    fribidi-dev \
    harfbuzz-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev 

COPY ./run.sh /run.sh

COPY . .

RUN ["chmod", "+x", "/run.sh"]
ENTRYPOINT ["/run.sh"]
