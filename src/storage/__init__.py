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
    _profiles: ProfilesTable
    _companies: CompaniesTable
    _sessions: SessionsTable
    _orders: OrdersTable
    _users: UsersTable
    _requests: RequestsTable

    def __init__(self, connection_url: str):
        core = StorageCore(connection_url)
        contacts = ContactsTable(core)
        profiles = ProfilesTable(core, contacts)
        self._companies = CompaniesTable(core, contacts)
        self._users = UsersTable(core, profiles)
        self._sessions = SessionsTable(core)
        self._requests = RequestsTable(core)
        self._orders = OrdersTable(core)
        self._contacts = contacts
        self._profiles = profiles

    def get_request_table(self):
        return self._requests

    def get_session_table(self):
        return self._sessions

    def get_order_table(self):
        return self._orders

    def get_users_table(self):
        return self._users

    def get_contacts_table(self):
        return self._contacts

    def get_profiles_table(self):
        return self._profiles

    def get_companies_table(self):
        return self._companies
