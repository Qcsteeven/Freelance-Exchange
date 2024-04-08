from ..storage_core import StorageCore
from .requests_table import RequestsTable
from .users_table import UsersTable


class OrdersTable:
    def __init__(self, core: StorageCore, requests: RequestsTable, users: UsersTable):
        self.db = core
        self.requests = requests
        self.users = users
