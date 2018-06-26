FROM alpine

MAINTAINER Reto Hasler <reto.hasler@asciich.ch>

RUN apk upgrade --no-cache && \
    apk update && \
    apk add --no-cache \
        git \
        py2-pip && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools