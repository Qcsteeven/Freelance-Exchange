from storage import Storage
from storage.tables import Table, TableInfoDict
from web.exceptions import NotFound
from .interfaces import ResponseJSON


class TmpDatabaseController:
    storage: Storage
    tables: dict[str, Table]

    def __init__(self, storage: Storage):
        self.storage = storage

        self.tables = {
            'users': storage.get_users_table(),
            'contacts': storage.get_contacts_table(),
            'profiles': storage.get_profiles_table(),
            'companies': storage.get_companies_table(),
            'sessions': storage.get_session_table(),
            'requests': storage.get_request_table(),
            'orders': storage.get_order_table()
        }

    def select_one(self, table: str, identifier: int):
        table_instance = self.tables.get(table)
        if table_instance is None:
            raise NotFound()
        return ResponseJSON(body=table_instance.select_one(identifier))

    def select_all(self, table: str):
        table_instance = self.tables.get(table)
        if table_instance is None:
            raise NotFound()
        return ResponseJSON(body=table_instance.select())

    def insert(self, table: str, info: TableInfoDict):
        table_instance = self.tables.get(table)
        if table_instance is None:
            raise NotFound()
        return ResponseJSON(body=table_instance.insert(info))

    def update(self, table: str, identifier: int, info: TableInfoDict):
        table_instance = self.tables.get(table)
        if table_instance is None:
            raise NotFound()
        return ResponseJSON(body=table_instance.update(identifier, info))

    def delete(self, table: str, identifier: int):
        table_instance = self.tables.get(table)
        if table_instance is None:
            raise NotFound()
        return ResponseJSON(body=table_instance.delete(identifier))
