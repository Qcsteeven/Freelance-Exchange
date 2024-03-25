from modules.companies_table import CompaniesTable
from modules.contacts_table import ContactsTable
from modules.sessions_table import SessionsTable
from modules.profiles_table import ProfilesTable
from modules.requests_table import RequestsTable
from modules.orders_table import OrdersTable
from modules.users_table import UsersTable
from storage_core import StorageCore

class Storage:

    def __init__(self, connection_url: str):
        core = StorageCore(connection_url)
        companies = CompaniesTable(core)
        contacts = ContactsTable(core)
        sessions = SessionsTable(core)
        profiles = ProfilesTable(core)
        requests = RequestsTable(core)
        orders = OrdersTable(core)
        users = UsersTable(core)