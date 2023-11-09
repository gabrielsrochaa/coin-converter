FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

COPY /poetry.lock /
COPY ./pyproject.toml /

RUN apt-get update -y && apt-get install curl -y \
&& curl -sSl https://install.python-poetry.org | python3 - \
&& poetry config virtualenvs.create false \
&& poetry install \
&& apt-get remove curl -y

COPY ./coin_converter_v2 /coin_converter_v2
WORKDIR /coin_converter_v2