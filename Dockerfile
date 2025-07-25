FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt


