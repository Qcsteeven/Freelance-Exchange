from ..storage_core import StorageCore

class UsersTable:
    def __init__(self, core: StorageCore):
        self.db = core