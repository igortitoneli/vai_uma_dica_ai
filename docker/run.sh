#!/bin/sh
export FLASK_APP=src/app.py

SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")
cd $DIR
. ./profile


echo
echo "Iniciando os containers no ambiente <$ENV>"
echo

docker compose -f docker-compose.yml  up --build -d
echo
docker compose ps
echo
