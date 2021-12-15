#!/bin/sh

# Wait for postgres service
if [ "$WAIT_FOR_SERVER" != "" ]; then
  echo "Waiting for server $WAIT_FOR_SERVER..."

  while ! nc -z "$WAIT_FOR_SERVER" "$WAIT_FOR_SERVER_PORT"; do
    sleep 0.1
  done

  echo "Server $WAIT_FOR_SERVER started"
fi

exec "$@"