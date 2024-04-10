from storage import Storage
from .interfaces import ResponseJSON


class TmpDatabaseController:
    storage: Storage

    def __init__(self, storage: Storage):
        self.storage = storage
        self.contacts = storage.get_contacts_table()

    def contacts_select_one(self, contact_id: int):
        return ResponseJSON(body=self.contacts.select_one(contact_id))

    def contacts_select_all(self):
        return ResponseJSON(body=self.contacts.select())

    def contacts_insert(self, email: str, telephone: str):
        return ResponseJSON(body=self.contacts.insert(email, telephone))

    def contacts_update(self, contact_id: int, email: str, telephone: str):
        contact_info = {
            'email': email,
            'telephone': telephone
        }
        return ResponseJSON(body=self.contacts.update(contact_id, contact_info))

    def contacts_delete(self, contact_id: int):
        return ResponseJSON(body=self.contacts.delete(contact_id))
