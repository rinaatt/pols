FROM python:3.6-slim

RUN apt-get update \
 && apt-get install -y gcc libc6-dev gettext sqlite3 --no-install-recommends \
 && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -U -r /tmp/requirements.txt

RUN groupadd -r django && useradd -r -g django django
RUN mkdir /var/web && chown django:django /var/web

# USER django:django
VOLUME /var/web
WORKDIR /var/web
