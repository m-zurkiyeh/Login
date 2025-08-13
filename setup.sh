#!/bin/bash

if (( $EUID != 0)); then
    echo Please run this script as root by using sudo
    exit
fi

apt update && upgrade
apt install gcc
apt install curl
apt install openssl
apt install mariadb-server
apt install libmariadb3 libmariadb-dev
apt install python3 python3-pip ipython3 python3-dev python3-venv