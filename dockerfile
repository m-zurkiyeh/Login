# syntax=docker/dockerfile:1

FROM python:3.11-slim@sha256:9e885f8239c31f8429448f933638dd13037c9119e2a362aeebdd37ec3bee7c85

WORKDIR /login


ENV PIP_ROOT_USER_ACTION=ignore


COPY . .
RUN chmod +x setup.sh
RUN ./setup.sh

RUN useradd -m myuser
USER myuser

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


EXPOSE 5000

CMD [ "python3", "-u","app.py"]

