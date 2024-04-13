from typing import TypedDict, Any
from psycopg import Connection
from ..storage_core import StorageCore
from ..exceptions import StorageException
from .contacts_table import ContactsTable, ContactInfo
from .table import Table


class CompaniesInfo(TypedDict):
    owner: int
    email: str | None
    telephone: str | None
    name: str
    description: str

class CompaniesInfoTransformed(TypedDict):
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
    table = 'companies'
    _properties = ['owner', 'contacts', 'name', 'description']
    _id = 'id'

    def __init__(self, core: StorageCore, contacts: ContactsTable):
        self.db = core
        self.contacts = contacts

    def _get_join_fragment(self) -> str:
        return f'LEFT JOIN {self.contacts.table} ON {self.table}.id={self.contacts.table}.contacts'

    def _get_join_properties(self) -> str:
        return f'{self.contacts.table}.email email, {self.contacts.table}.telephone telephone'

    def _insert_before(self, con: Connection, info: CompaniesInfo) -> CompaniesInfoTransformed:
        contact = self.contacts.insert_with_con(
            con,
            ContactInfo(email=info['email'], telephone=info['telephone'])
        )
        return CompaniesInfoTransformed(
            owner=info['owner'],
            contacts=contact['id'],
            name=info['name'],
            description=info['description']
        )

    def _update_before(self, con, identifier: int, info: CompaniesInfo) -> CompaniesInfoTransformed:
        company = self.select_one(identifier)

        if company is None:
            raise StorageException('Not Found')

        self.contacts.update_with_con(
            con,
            company['contacts'],
            ContactInfo(email=info['email'], telephone=info['telephone'])
        )

        return CompaniesInfoTransformed(
            owner=info['owner'],
            contacts=company['contacts'],
            name=info['name'],
            description=info['description']
        )

    def _get_values(self, info: CompaniesInfoTransformed) -> list[Any]:
        return [info['owner'], info['contacts'], info['name'], info['description']]

    def _get_zero_row(self) -> CompaniesRow:
        return CompaniesRow(
            id=0,
            owner=0,
            contacts=0,
            name='Not Found',
            description='Not Found'
        )
