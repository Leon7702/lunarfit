#!/usr/bin/env sh

# check for new python deps
# python3.9 -m pip install -r requirements.txt

# run database migrations
python3.9 manage.py migrate --no-input

# load all fixtures in default fixtures directory of apps
python3.9 manage.py loaddata ./*/fixtures/*.yaml

# collect static assets in ./dist dir
python3.9 manage.py collectstatic --no-input

# Run the gunicorn prod server this will take the default 127.0.0.1:8000
# if there isn't a gunicorn.conf.py
gunicorn lunarfit.wsgi
