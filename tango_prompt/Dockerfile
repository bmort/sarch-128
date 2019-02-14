#
# Docker Image: skasiid/tango_prompt
#
# This Dockerfile creates a Docker Image used to provide a terminal prompt
# with iTango installed.
#
FROM skasiid/tango_docker_base:0.1.0
LABEL maintainer="Benjamin Mort <ben.mort@gmail.com>"

USER root
RUN pip3 install \
    itango==0.1.6 \
    skasip-logging==1.0.14

USER siid
RUN mkdir ~/.ipython
ENV TANGO_HOST=localhost:10000

ENTRYPOINT ["/bin/bash"]
