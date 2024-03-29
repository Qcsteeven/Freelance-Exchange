from contacts_table import ContactsTable
from ..storage_core import StorageCore


class CompaniesTable:
    def __init__(self, core: StorageCore, contacts: ContactsTable):
        self.db = core
        self.contacts = contacts
