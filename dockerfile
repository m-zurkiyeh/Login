# syntax=docker/dockerfile:1

FROM python:3.11-slim@sha256:9e885f8239c31f8429448f933638dd13037c9119e2a362aeebdd37ec3bee7c85

WORKDIR /login

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && apt-get install -y  --no-install-recommends \
    python3-pip \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    libmariadb3 \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN useradd -m myuser
USER myuser

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p templates

EXPOSE 5000



#CMD [ "python3", "-u","main.py"]

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
