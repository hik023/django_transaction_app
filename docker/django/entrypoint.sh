#!/usr/bin/env bash
python manage.py wait_for_database &&
python manage.py migrate --noinput &&
python manage.py test &&
python -m gunicorn django_transaction_app.wsgi:application --bind 0.0.0.0:8000 --reload