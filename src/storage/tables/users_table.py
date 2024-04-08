from ..storage_core import StorageCore
from .companies_table import CompaniesTable
from .profiles_table import ProfilesTable
from .requests_table import RequestsTable


class UsersTable:
    def __init__(self, core: StorageCore, profiles: ProfilesTable, companies: CompaniesTable, requests: RequestsTable):
        self.db = core
        self.profiles = profiles
        self.companies = companies
        self.requests = requests
