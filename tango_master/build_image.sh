#!/usr/bin/env bash
# Script to build and upload the SKA SIID SDP Tango Master image.

RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

VERSION="$(python -c "from src.release import __version__; print(__version__)")"

IMAGE=skasiid/tango_master

echo -e "${RED}---------------------------------------------------------${NC}"
echo -e "${BLUE}Building and uploading Docker image(s):"
echo -e "${BLUE}    - ${IMAGE}:${VERSION}"
echo -e "${BLUE}    - ${IMAGE}:latest"
echo -e "${RED}---------------------------------------------------------${NC}"

docker build -t ${IMAGE}:"${VERSION}" .
docker tag ${IMAGE}:"${VERSION}" ${IMAGE}:latest
docker push ${IMAGE}:"${VERSION}"
docker push ${IMAGE}:latest
