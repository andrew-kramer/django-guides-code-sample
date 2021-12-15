#!/bin/bash

function generatePassword() {
    openssl rand -base64 16
}

function generateAppKey() {
    openssl rand -base64 32
}

if [ "$1" = "" ]
then
  echo "Usage: $(basename "$0") [dev|test|prod]"
  exit 1
elif [ "$1" != "dev" ] && [ "$1" != "test" ] && [ "$1" != "prod" ]
then
  echo "Usage: $(basename "$0") [dev|test|prod]"
  exit 1
fi

if [ ! -f "$(dirname "$0")/$1.env" ]
then
  cp "$(dirname "$0")/.env.example" "$(dirname "$0")/$1.env"
fi

APPLICATION_KEY=$(generateAppKey)
POSTGRES_PASSWORD=$(generatePassword)
SUPERUSER_PASSWORD=$(generatePassword)

sed -i.bak \
    -e "s#APPLICATION_KEY=.*#APPLICATION_KEY=\"base64:${APPLICATION_KEY}\"#g" \
    -e "s#POSTGRES_PASSWORD=.*#POSTGRES_PASSWORD=\"${POSTGRES_PASSWORD}\"#g" \
    "$(dirname "$0")/$1.env"

if [ "$1" = "dev" ]; then
sed -i \
    -e "s#APP_SUPERUSER_PASSWORD=.*#APP_SUPERUSER_PASSWORD=\"${SUPERUSER_PASSWORD}\"#g" \
    "$(dirname "$0")/$1.env"
fi