from typing import TypedDict, Any
from psycopg import Connection
from ..storage_core import StorageCore
from ..exceptions import StorageException
from .profiles_table import ProfilesTable, ProfileInfo
from .table import Table


class UserInfo(TypedDict):
    is_customer: bool
    # profile table
    email: str | None
    telephone: str | None
    first_name: str
    second_name: str | None
    skills: list[str]

class UserInfoTransformed(TypedDict):
    profile: int
    is_customer: bool

class UserRow(TypedDict):
    id: int
    is_customer: bool
    # profile table
    email: str | None
    telephone: str | None
    first_name: str
    second_name: str | None
    skills: list[str]

class UsersTable(Table[UserInfo, UserInfoTransformed, UserRow]):
    table = 'users'
    _properties = ['profile', 'is_customer']
    _id = 'id'

    def __init__(self, core: StorageCore, profiles: ProfilesTable):
        self.db = core
        self.profiles = profiles

    def _get_join_fragment(self) -> str:
        return f'LEFT JOIN ({self.profiles.get_select_sql()}) pf ON pf.id={self.table}.profile'

    def _get_join_properties(self) -> str:
        return f'pf.email email, pf.telephone telephone, pf.first_name first_name, pf.second_name second_name, pf.skills skills'

    def _insert_before(self, con: Connection, info: UserInfo) -> UserInfoTransformed:
        profile = self.profiles.insert_with_con(con, ProfileInfo(
            email=info['email'],
            telephone=info['telephone'],
            first_name=info['first_name'],
            second_name=info['second_name'],
            skills=info['skills']
        ))
        return UserInfoTransformed(
            profile=profile['id'],
            is_customer=info['is_customer']
        )

    def _update_before(self, con: Connection, identifier: int, info: UserInfo) -> UserInfoTransformed:
        user = self.select_one(identifier)

        if user is None:
            raise StorageException('Not Found')

        self.profiles.update_with_con(con, user['profile'], ProfileInfo(
            email=info['email'],
            telephone=info['telephone'],
            first_name=info['first_name'],
            second_name=info['second_name'],
            skills=info['skills']
        ))

        return UserInfoTransformed(
            profile=user['profile'],
            is_customer=info['is_customer']
        )

    def _get_values(self, info: UserInfoTransformed) -> list[Any]:
        return [info['profile'], info['is_customer']]

    def _get_zero_row(self) -> UserRow:
        return UserRow(id = 0, profile=0, is_customer=False)
