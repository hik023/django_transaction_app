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
Service will be available at http://localhost
> [!WARNING]
> If you got **502 Bad gateway** error, wait until django service start (~15-30 sec)
## Fill with test data
On running service
```shell
docker compose exec django python manage.py fill_with_data

```

## Stop service
```shell
docker compose stop

```