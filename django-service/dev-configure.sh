#!/bin/sh

echo "Performing dev environment configuration..."

echo ""
echo "Importing fixtures..."

if [ -f fixtures.json ]; then
  python manage.py loaddata fixtures.json
fi