from typing import TypedDict, Any
from ..storage_core import StorageCore
from .contacts_table import ContactsTable
from .table import Table


class CompaniesInfo(TypedDict):
    owner: int

    name: str
    description: str

class CompaniesInfoTransformed(TypedDict):
    id: int
    owner: int
    contacts: int
    name: str
    description: str

class CompaniesRow(TypedDict):
    id: int
    owner: int
    contacts: int
    name: str
    description: str


class CompaniesTable(Table[CompaniesInfo, CompaniesInfoTransformed, CompaniesRow]):
    _table = 'companies'
    _properties = ['owner', 'contacts', 'name', 'description']
    _id = 'id'

    def __init__(self, core: StorageCore, contacts: ContactsTable):
        self.db = core
        self.contacts = contacts

    def _insert_before(self, con, info: CompaniesInfo) -> CompaniesInfoTransformed:
        return info

    def _update_before(self, con, identifier: int, info: CompaniesInfo) -> CompaniesInfoTransformed:
        return info

    def _get_values(self, info: CompaniesInfo) -> list[Any]:
        return []

    def _get_zero_row(self) -> CompaniesRow:
        return CompaniesRow()