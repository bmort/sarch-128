FROM skasiid/tango_docker_base:0.1.0
LABEL maintainer="Benjamin Mort <ben.mort@gmail.com>"

USER root

COPY requirements.txt .
RUN pip3 install -r requirements.txt

USER siid

COPY src app

ENTRYPOINT ["./app/processing_block_ds.py"]
CMD ["1", "-v4"]
