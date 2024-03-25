from ..storage_core import StorageCore

class ContactsTable:
    def __init__(self, core: StorageCore):
        self.db = core