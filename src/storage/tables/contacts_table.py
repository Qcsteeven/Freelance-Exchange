from typing import TypedDict
from ..storage_core import StorageCore


class ContactInfo(TypedDict):
    email: str | None
    telephone: str | None

class ContactRow(TypedDict):
    id: int
    email: str | None
    telephone: str | None

zero_contact_row = ContactRow(id=0, email=None, telephone=None)

class ContactsTable:
    _db: StorageCore

    def __init__(self, core: StorageCore):
        self._db = core

    def select_raw(self) -> str:
        return 'SELECT * FROM contacts'

    def select(self) -> list[ContactRow]:
        with self._db.get_select_cursor() as cursor:
            cursor.execute(self.select_raw())
            return cursor.fetchall()

    def select_one(self, contact_id: int) -> None | ContactRow:
        with self._db.get_select_cursor() as cursor:
            cursor.execute(f'{self.select_raw()} WHERE id=%s', [contact_id])
            return cursor.fetchone()

    def insert(self, email: str, telephone: str) -> ContactRow:
        values = [email, telephone]

        with self._db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO contacts (mail, telephone) VALUES (%s, %s) RETURNING id, mail, telephone',
                    values
                )
                result = cursor.fetchone()
                return result if result else zero_contact_row

    def update(self, contact_id: int, info: ContactInfo) -> None | ContactRow:
        values = [info['email'], info['telephone'], contact_id]

        with self._db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE contacts SET mail=%s, telephone=%s WHERE id=%s RETURNING id, mail, telephone',
                    values
                )
                return cursor.fetchone()

    def delete(self, contact_id: int) -> None | ContactRow:
        with self._db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM contacts WHERE id=%s RETURNING id, mail, telephone', [contact_id])
                result = cursor.fetchone()
                return result if result else zero_contact_row
