from ..storage_core import StorageCore

class OrdersTable:
    def __init__(self, core: StorageCore):
        self.db = core