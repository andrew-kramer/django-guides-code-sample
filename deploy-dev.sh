#!/usr/bin/env bash

if [[ $* == *--build* ]]; then
  BUILD="--build"
else
  BUILD=""
fi


if [[ $* == *--clean* ]]; then
  echo "Building clean..."
  docker rm django-guides-dev_db_1 django-guides-dev_web_1 django-guides-dev_nginx_1 django-guides-dev_frontend_1 \
  django-guides-dev_redis_1
  docker volume prune -f
  docker-compose -f docker-compose-dev.yml -f docker-compose-override-clean.yml -p django-guides-dev up $BUILD
else
  echo "Building unclean..."
  docker-compose -f docker-compose-dev.yml -p django-guides-dev up $BUILD
fi
