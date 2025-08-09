# syntax=docker/dockerfile:1

FROM python:3.11-slim

WORKDIR /login

RUN apt-get update && apt-get install -y \
    python3-pip \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    libmariadb3 \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p templates

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

#CMD [ "python3", "-u","main.py"]

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
