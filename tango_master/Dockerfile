FROM skasiid/tango_docker_base:0.1.0
LABEL maintainer="Benjamin Mort <ben.mort@gmail.com>"

USER root

COPY requirements.txt .
RUN pip3 install -r requirements.txt

USER siid

COPY src app

HEALTHCHECK --interval=30s --retries=3 --timeout=10s \
  CMD python3 -c "import tango; d = tango.DeviceProxy('localhost:10000/siid_sdp/elt/master#dbase=no'); d.ping()" || exit 1

ENTRYPOINT ["./app/sdp_master_ds.py"]
CMD ["1", "-v4"]
# CMD ["1", "-v4", "-nodb", "-ORBendPoint", "giop:tcp:10000"]
