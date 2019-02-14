#!/usr/bin/env bash

docker run --rm -d --name tango_master \
    -p 10000:10000 \
    skasiid/tango_master:0.1.0 \
    1 -v4 -nodb -ORBendPoint giop:tcp::10000 -dlist siid_sdp/elt/master
