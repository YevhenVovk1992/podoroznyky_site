FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /flask_app

COPY requirements.txt /flask_app/
RUN pip install -r requirements.txt

COPY . /flask_app/
