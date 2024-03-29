# Freelance-Exchange

## Initializing the Project

### Installing dependencies

```bash
python -m venv .venv
pip install poetry
poetry shell
poetry install
```

### Server configuration settings

To configure the server, use the .env file

The repository does not have all the settings and to start the server. You need to copy the .env.example template, and rename it to .env, then fill in the missing fields.

### Initialize DataBase

Before initializing the database, you need to create an .env file.

To initialize and work with the database, you need to install docker and docker-compose.

The following command initializes the database and when the database write message 'database system is ready to accept connections', it can be turned off via CTRL + C.

```bash
docker-compose -f dc-init.yml up
```

After this we must completely remove the container with the command.

```bash
docker-compose -f dc-init.yml down
```

## Launch of the project

### Running in development mode

To run in development mode, you need to enable the database using docker.

```bash
docker-compose -f docker-compose.dev.yml up
```

Чтобы запустить сам сервер, используйте эту команду

```bash
python src/main.py
```

After work you need to shut down the database

```bash
docker-compose -f docker-compose.dev.yml down
```