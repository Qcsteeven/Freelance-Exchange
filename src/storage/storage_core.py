from psycopg.rows import dict_row
import psycopg


# Данный класс является singleton
class StorageCore:
    _instance = None
    _select_connection: psycopg.Connection
    _connection_url: str

    def __init__(self, connection_url: str):
        self._connection_url = connection_url
        self._select_connection = psycopg.connect(connection_url, autocommit=True, row_factory=dict_row)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_select_connection(self) -> psycopg.Connection:
        return self._select_connection

    def get_select_cursor(self) -> psycopg.Cursor:
        return self._select_connection.cursor()

    def get_connection(self) -> psycopg.Connection:
        return psycopg.connect(self._connection_url, row_factory=dict_row)
