from modules.companies_table import CompaniesTable
from modules.contacts_table import ContactsTable
from modules.sessions_table import SessionsTable
from modules.profiles_table import ProfilesTable
from modules.requests_table import RequestsTable
from modules.orders_table import OrdersTable
from modules.users_table import UsersTable
from storage_core import StorageCore

class Storage:
    _contacts: ContactsTable
    _sessions: SessionsTable
    _orders: OrdersTable

    def __init__(self, connection_url: str):
        core = StorageCore(connection_url)
        requests = RequestsTable(core)
        contacts = ContactsTable(core)
        self._sessions = SessionsTable(core)
        companies = CompaniesTable(core, contacts)
        profiles = ProfilesTable(core, contacts)
        users = UsersTable(core, profiles, companies, requests)
        self._orders = OrdersTable(core, requests, users)
        self._contacts = contacts

    def get_contacts_table(self):
        return self._contacts
