FROM ubuntu:18.04
LABEL maintainer="Benjamin Mort <ben.mort@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3-pytango python3-pip

RUN useradd -ms /bin/bash siid
USER siid
WORKDIR /home/siid
