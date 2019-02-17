FROM skasiid/tango_docker_base:0.1.0
LABEL maintainer="Benjamin Mort <ben.mort@gmail.com>"

USER root
RUN apt-get update && apt-get install -y git
RUN pip3 install \
    skasip-logging==1.0.14 \
    itango==0.1.6 \
    codecov==2.0.15 \
    coverage==4.5.2 \
    coveralls==1.5.1 \
    pytest==4.0.1 \
    pytest-pylint==0.13.0 \
    pytest-codestyle==1.3.1 \
    pytest-pydocstyle==1.4.1 \
    pytest-cov==2.6.0

# COPY setup.cfg .
# COPY run_test.sh .

# ENV TANGO_HOST=localhost:10000
# RUN mkdir ~/.ipython
