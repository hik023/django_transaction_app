FROM python:3.10.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./django_transaction_app /app/django_transaction_app

RUN apt-get install gcc default-libmysqlclient-dev -y

COPY ./docker/django/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# CMD ["python", "django_transaction_app/manage.py", "runserver"]

COPY ./docker/django/entrypoint.sh /app/entrypoint.sh

RUN chmod 777 /app/entrypoint.sh

WORKDIR /app/django_transaction_app

RUN ./manage.py collectstatic --noinput --clear

ENTRYPOINT ["/app/entrypoint.sh"]

# CMD ["uvicorn", "django_transaction_app.django_transaction_app.asgi:application", "--host", "0.0.0.0", "--port", "8000"]