#!/usr/bin/env bash
RED='\033[0;31m'
NC='\033[0m'

DIR="$1"
OPTIONS=("${@:2}")

if [[ -n "${OPTIONS[*]}" && "${OPTIONS[0]}" == "--tests-only" ]]; then
    CMD="python3 -m pytest -s -vv \
        --rootdir=. \
        ${OPTIONS[*]} \
        ${DIR}"
elif [[ -n "${OPTIONS[*]}" && "${OPTIONS[0]}" == "--no-cov" ]]; then
    CMD="python3 -m pytest -s -vv \
        --rootdir=. \
        --pylint \
        --codestyle \
        --docstyle \
        ${OPTIONS[*]} \
        ${DIR}"
elif [[ -n "${OPTIONS[*]}" ]]; then
    CMD="python3 -m pytest -s -vv \
        --rootdir=. \
        --pylint \
        --codestyle \
        --docstyle \
        --cov-config=./tools/setup.cfg \
        --cov-append \
        --cov-branch \
        --no-cov-on-fail \
        --cov=${DIR} \
        ${OPTIONS[*]} \
        ${DIR}"
else
    CMD="python3 -m pytest -s -vv \
        --rootdir=. \
        --pylint \
        --codestyle \
        --docstyle \
        --cov-config=./tools/setup.cfg \
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
