#!/usr/bin/env bash
DIR="$1"
RED='\033[0;31m'
NC='\033[0m'

if [[ $2 == "--tests-only" ]]; then
    CMD="python3 -m pytest -s -vv \
        --rootdir=. \
        --cov-config=./tango_tests/setup.cfg \
        --cov-append \
        --cov-branch \
        --no-cov-on-fail \
        --cov=${DIR} \
         ${DIR}"
else
    CMD="python3 -m pytest -s -vv \
        --rootdir=. \
        --pylint \
        --codestyle \
        --docstyle \
        --cov-config=./tango_tests/setup.cfg \
        --cov-append \
        --cov-branch \
        --no-cov-on-fail \
        --cov=${DIR} \
        ${DIR}"
fi


echo -e "${RED}---------------------------------------${NC}"
echo -e "${CMD}"
echo -e "${RED}---------------------------------------${NC}"

eval "${CMD}"
