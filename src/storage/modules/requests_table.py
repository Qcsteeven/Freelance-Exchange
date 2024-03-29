from ..storage_core import StorageCore

class RequestsTable:
    def __init__(self, core: StorageCore):
        self.db = core
