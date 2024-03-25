import psycopg

# Данный класс является singleton
class StorageCore:
    _instance = None

    def __init__(self, connection_url: str):
        try:
            self.connection = psycopg.connect(connection_url)
        except:
            print('Failed to connect to database.')


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
