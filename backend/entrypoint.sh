#!/usr/bin/env sh

# generate and run database migrations
python3 manage.py makemigrations
python3 manage.py migrate

# load all fixtures in default fixtures directory of apps
python3 manage.py loaddata ./*/fixtures/*.yaml

# Run the dev server on 0.0.0.0 to make it accessible outside the container
python3 manage.py runserver 0.0.0.0:8000
