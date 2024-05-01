# Django transactions service
Provides the ability to manage transactions and wallets

## Build
```shell
docker compose build
```

## Run
```shell
docker compose up -d
```

## Fill with test data
On running container
```shell
docker compose exec django python manage.py fill_with_data

```