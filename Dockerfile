# ========= pull official base image ========
FROM python:3.12-slim

# ========= set work directory ========
WORKDIR /django_app

# ========= set environment variables ========
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ========= install dependencies ========
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# ========= COPY project ========
COPY . .
