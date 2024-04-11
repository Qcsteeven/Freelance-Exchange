from typing import TypedDict, Any
from .table import Table


class ContactInfo(TypedDict):
    email: str | None
    telephone: str | None

class ContactRow(TypedDict):
    id: int
    email: str | None
    telephone: str | None

class ContactsTable(Table[ContactInfo, ContactInfo, ContactRow]):
    _table = 'contacts'
    _properties = ['email', 'telephone']
    _id = 'id'

    def _insert_before(self, con, info: ContactInfo) -> ContactInfo:
        return info

    def _update_before(self, con, identifier: int, info: ContactInfo) -> ContactInfo:
        return info

    def _get_values(self, info: ContactInfo) -> list[Any]:
        return [info['email'], info['telephone']]

    def _get_zero_row(self) -> ContactRow:
        return ContactRow(id = 0, email=None, telephone=None)
