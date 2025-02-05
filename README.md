# test-automation

## Install Pre-Commits

```shell
pre-commit install
```

# Run
```shell
docker build -t test-automation/base .
```

```shell
docker run -it -v $(pwd):/app -w /app test-automation/base:latest poetry add [name-libs]
```

```shell
docker run -it -v $(pwd):/app -w /app test-automation/base:latest poetry update --lock
```

## Update requirements.txt

```shell
docker run -it -v $(pwd):/app -w /app test-automation/base:latest poetry export --without-hashes -o requirements.txt
```
## Development
```shell
docker run -it -v $(pwd):/app -w /app test-automation/base:latest poetry export --without-hashes --with ozon -o requirements.ozon.txt
```


## Run server
```shell
docker-compose up --build
```
