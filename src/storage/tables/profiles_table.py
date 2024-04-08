from ..storage_core import StorageCore
from .contacts_table import ContactsTable


class ProfilesTable:
    def __init__(self, core: StorageCore, contacts: ContactsTable):
        self.db = core
        self.contacts = contacts
