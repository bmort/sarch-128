#!/usr/bin/env bash
#
# Script to build an upload the SIID Tango Docker base image.
#

RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

VERSION="0.1.0"
IMAGE=skasiid/tango_docker_base
echo -e "${RED}---------------------------------------------------------${NC}"
echo -e "${BLUE}Building and uploading Docker image(s):"
echo -e "${BLUE}    - ${IMAGE}:${VERSION}"
echo -e "${BLUE}    - ${IMAGE}:latest"
echo -e "${RED}---------------------------------------------------------${NC}"

docker build -t ${IMAGE}:${VERSION} .
docker tag ${IMAGE}:${VERSION} ${IMAGE}:latest
docker push ${IMAGE}:${VERSION}
docker push ${IMAGE}:latest
