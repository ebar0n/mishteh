FROM python:3.7

RUN apt-get update && apt-get install -y postgresql-client \
    gcc gettext \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
