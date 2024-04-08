from .storage_core import StorageCore
from .tables.companies_table import CompaniesTable
from .tables.contacts_table import ContactsTable
from .tables.sessions_table import SessionsTable
from .tables.profiles_table import ProfilesTable
from .tables.requests_table import RequestsTable
from .tables.orders_table import OrdersTable
from .tables.users_table import UsersTable

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
