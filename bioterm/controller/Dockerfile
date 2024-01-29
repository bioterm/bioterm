FROM python:3.11

WORKDIR /

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY bioterm/common /bioterm/common

COPY bioterm/controller /bioterm/controller
