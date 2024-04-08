from dataclasses import dataclass
from ..storage_core import StorageCore


@dataclass
class ContactInfo:
    mail: str | None
    telephone: str | None

class ContactsTable:
    _db: StorageCore

    def __init__(self, core: StorageCore):
        self._db = core

    def select_raw(self) -> str:
        return 'SELECT * FROM contacts'

    def select(self):
        connection = self._db.get_select_connection()
        with connection.cursor() as cursor:
            cursor.execute(self.select_raw())
            return cursor.fetchall()

    def insert(self, mail: str, telephone: str) -> int:
        values = [mail, telephone]

        with self._db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO contacts (mail, telephone) VALUES (%s, %s) RETURNING id', values)
                print(cursor.fetchone())
                return 1

    def update(self, contact_id: int, info: ContactInfo):
        values = [info.mail, info.telephone, contact_id]

        with self._db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute('UPDATE SET mail=%s telephone=%s WHERE id=%s', values)
