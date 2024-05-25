from typing import TypedDict, Any
from psycopg import Connection
from ..storage_core import StorageCore
from ..exceptions import StorageException
from .contacts_table import ContactsTable, ContactInfo
from .table import Table


class ProfileInfo(TypedDict):
    owner: int
    email: str | None
    telephone: str | None
    first_name: str
    second_name: str | None
    skills: list[str] | None

class ProfileInfoTransformed(TypedDict):
    owner: int
    contacts: int
    first_name: str
    second_name: str | None
    skills: list[str]

class ProfileRow(TypedDict):
    id: int
    owner: int
    contacts: int
    first_name: str
    second_name: str | None
    skills: list[str]

class ProfilesTable(Table[ProfileInfo, ProfileInfoTransformed, ProfileRow]):
    table = 'profiles'
    _properties = ['owner', 'contacts', 'first_name', 'second_name', 'skills']
    _id = 'id'

    def __init__(self, core: StorageCore, contacts: ContactsTable):
        super().__init__(core)
        self.contacts = contacts

    def _get_join_fragment(self) -> str:
        return f'LEFT JOIN {self.contacts.table} ON {self.contacts.table}.id={self.table}.contacts'

    def _get_join_properties(self) -> str:
        return f'{self.contacts.table}.email email, {self.contacts.table}.telephone telephone'

    def _insert_before(self, con: Connection, info: ProfileInfo) -> ProfileInfoTransformed:
        contact = self.contacts.insert_with_con(
            con,
            ContactInfo(email=info['email'], telephone=info['telephone'])
        )

        skills = info['skills']

        if skills is None:
            skills = []

        return ProfileInfoTransformed(
            contacts=contact['id'],
            owner=info['owner'],
            first_name=info['first_name'],
            second_name=info['second_name'],
            skills=skills
        )

    def _update_before(self, con: Connection, identifier: int, info: ProfileInfo) -> ProfileInfoTransformed:
        profile = self.select_one(identifier)

        if profile is None:
            raise StorageException('Not Found')

        self.contacts.update_with_con(
            con,
            profile['contacts'],
            ContactInfo(email=info['email'], telephone=info['telephone'])
        )

        skills = info['skills']

        if skills is None:
            skills = []

        return ProfileInfoTransformed(
            owner=info['owner'],
            contacts=profile['contacts'],
            first_name=info['first_name'],
            second_name=info['second_name'],
            skills=skills
        )

    def _delete_after(self, con: Connection, row: ProfileInfoTransformed):
        self.contacts.delete_with_con(con, row['contacts'])

    def _get_values(self, info: ProfileInfoTransformed) -> list[Any]:
        return [info['owner'], info['contacts'], info['first_name'], info['second_name'], info['skills']]

    def _get_zero_row(self) -> ProfileInfoTransformed:
        return ProfileInfoTransformed(owner=0, contacts=0, first_name='not found', second_name=None, skills=[])
