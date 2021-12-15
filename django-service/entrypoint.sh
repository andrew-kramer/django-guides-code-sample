#!/bin/sh

# Wait for postgres service
if [ "$WAIT_FOR_SERVER" != "" ]; then
  echo "Waiting for server $WAIT_FOR_SERVER..."

  while ! nc -z "$WAIT_FOR_SERVER" "$WAIT_FOR_SERVER_PORT"; do
    sleep 0.1
  done

  echo "Server $WAIT_FOR_SERVER started"
fi

# In DEV environment only, automatically handle some installation
if [ "$APP_ENVIRONMENT" = "dev" ] && [ "$DO_DEV_INSTALLS" = "true" ]; then
  ./dev-install.sh
fi

if [ "$SKIP_DATABASE_SETUP" != "true" ]; then
  # Make migrations and migrate the database.
  echo "Making migrations and migrating the database. "
  python manage.py makemigrations --noinput
  python manage.py migrate --noinput
fi

# In DEV environment only, automatically handle some configuration
if [ "$APP_ENVIRONMENT" = "dev" ] && [ "$DO_DEV_CONFIGS" = "true" ]; then
  ./dev-configure.sh
fi

if [ "$SKIP_STATIC_FILES" != "true" ]; then
  # Collect the static files and make them accessible for nginx
  # This is necessary because we use a volume even in production
  python manage.py collectstatic --noinput
fi

exec "$@"