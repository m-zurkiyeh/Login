#!/bin/bash

if (( $EUID != 0)); then
    echo Please run this script as root by using sudo
    exit
fi

#apt-get update && apt-get upgrade
#apt-get install -y --no-install-recommends gcc curl openssl mariadb-server libmariadb3 libmariadb-dev python3 python3-pip ipython3 python3-dev python3-venv gunicorn pkg-config


RUN apt-get update && apt-get install -y --no-install-recommends \
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
    && rm -rf /var/lib/apt/lists/*