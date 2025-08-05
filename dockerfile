# syntax=docker/dockerfile:1

FROM python:3.11-slim

RUN mkdir /login 

WORKDIR /login

RUN apt update && apt install python3-pip libmariadb3 libmariadb-dev -y


COPY . .

RUN pip install -r requirements.txt --break-system-packages


#CMD [ "python3", "-u","main.py"]

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
