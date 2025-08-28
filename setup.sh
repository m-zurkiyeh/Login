#!/bin/bash

if (( $EUID != 0)); then
    echo Please run this script as root by using sudo
    exit
fi

<<<<<<< HEAD
#apt-get update && apt-get upgrade
#apt-get install -y --no-install-recommends gcc curl openssl mariadb-server libmariadb3 libmariadb-dev python3 python3-pip ipython3 python3-dev python3-venv gunicorn pkg-config


RUN apt-get update && apt-get install -y --no-install-recommends \
=======
apt-get update && apt-get install -y --no-install-recommends \
>>>>>>> 70c5dfe9af3de180fd9f0be3974df3af581b5119
    gcc \
    libmariadb3 \
    libmariadb-dev \
    python3 \
    python3-pip \
    ipython3 \
    python3-dev \
    python3-venv \
    gunicorn \
    pkg-config \
<<<<<<< HEAD
    && rm -rf /var/lib/apt/lists/*
=======
    && rm -rf /var/lib/apt/lists/*
#apt-get install -y --no-install-recommends gcc curl openssl mariadb-server libmariadb3 libmariadb-dev python3 python3-pip ipython3 python3-dev python3-venv gunicorn pkg-config
>>>>>>> 70c5dfe9af3de180fd9f0be3974df3af581b5119
