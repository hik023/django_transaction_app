#!/usr/bin/env bash
sleep 10 &&
# python django_transaction_app/manage.py migrate --noinput &&
python -m uvicorn django_transaction_app.asgi:application --host 0.0.0.0 --port 8000 