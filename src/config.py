import os
from dotenv import load_dotenv

class ConfigParseException(Exception):
    "Config Parse Exception"

class Config:
    _db_host: str
    _db_port: int
    _db_user: str
    _db_password: str
    _db_name: str
    _server_port: int

    def __init__(self):
        self._init_dotenv_to_environment()
        self._init_from_environment()

    def _init_dotenv_to_environment(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

        if not os.path.exists(dotenv_path):
            raise ConfigParseException("Don't has .env file. Added .env file with required environments.")

        load_dotenv(dotenv_path)

    def _init_from_environment(self):
        try:
            self._db_host = os.environ.get('DB_HOST').strip()
            self._db_port = int(os.environ.get('DB_PORT').strip())
            self._db_user = os.environ.get('DB_USER').strip()
            self._db_password = os.environ.get('DB_PASSWORD').strip()
            self._db_name = os.environ.get('DB_NAME').strip()
            self._server_port = int(os.environ.get('SERVER_PORT'))

            properties = [
                not self._db_host, not self._db_port, not self._db_user,
                not self._db_password, not self._db_name, self._server_port
            ]

            if True in properties:
                raise ConfigParseException()
        except (ConfigParseException, ValueError, TypeError) as e:
            raise ConfigParseException(
                'Invalid .env file. It is necessary to fix errors and unspecified environment variables.'
            ) from e

    def get_database_url(self) -> str:
        return f'postgres://{self._db_user}:{self._db_password}@{self._db_host}:{self._db_port}/{self._db_name}'

    def get_server_port(self):
        return self._server_port
