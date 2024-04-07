from ..storage_core import StorageCore

class SessionsTable:
    def __init__(self, core: StorageCore):
        self.db = core
