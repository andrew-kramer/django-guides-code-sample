#!/bin/sh

echo "Performing dev environment installations..."

echo ""
echo "Updating pip requirements..."

pip install --upgrade pip
pip install -r requirements.txt
