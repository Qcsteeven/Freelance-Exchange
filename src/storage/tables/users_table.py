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
    skills: list[str] | None

class UserInfoTransformed(TypedDict):
    is_customer: bool

class UserRow(TypedDict):
    id: int
    is_customer: bool
    # profile table
    profile: int
    email: str | None
    telephone: str | None
    first_name: str
    second_name: str | None
    skills: list[str]

class UsersTable(Table[UserInfo, UserInfoTransformed, UserRow]):
    table = 'users'
    _properties = ['is_customer']
    _id = 'id'

    def __init__(self, core: StorageCore, profiles: ProfilesTable):
        super().__init__(core)
        self.profiles = profiles

    def _get_join_fragment(self) -> str:
        return f'LEFT JOIN ({self.profiles.get_select_sql()}) pf ON pf.owner={self.table}.id'

    def _get_join_properties(self) -> str:
        first_part = 'pf.email email, pf.telephone telephone, pf.first_name first_name'
        second_part = ', pf.second_name second_name, pf.skills skills, pf.id profile'
        return f'{first_part}{second_part}'

    def _insert_before(self, con: Connection, info: UserInfo) -> UserInfoTransformed:
        return UserInfoTransformed(
            is_customer=info['is_customer']
        )

    def _insert_after(self, con: Connection, identifier: int, info: UserInfo):
        self.profiles.insert_with_con(con, ProfileInfo(
            owner=identifier,
            email=info['email'],
            telephone=info['telephone'],
            first_name=info['first_name'],
            second_name=info['second_name'],
            skills=info['skills']
        ))

    def _update_before(self, con: Connection, identifier: int, info: UserInfo) -> UserInfoTransformed:
        user = self.select_one(identifier)

        if user is None:
            raise StorageException('Not Found')

        self.profiles.update_with_con(con, user['profile'], ProfileInfo(
            owner=identifier,
            email=info['email'],
            telephone=info['telephone'],
            first_name=info['first_name'],
            second_name=info['second_name'],
            skills=info['skills']
        ))

        return UserInfoTransformed(
            is_customer=info['is_customer']
        )

    def _delete_before(self, con: Connection, identifier: int):
        result = con.execute(f'SELECT * FROM {self.profiles.table} WHERE owner=%s', [identifier]).fetchone()
        self.profiles.delete_with_con(con, result.get('id'))

    def _get_values(self, info: UserInfoTransformed) -> list[Any]:
        return [info['is_customer']]

    def _get_zero_row(self) -> UserInfoTransformed:
        return UserInfoTransformed(is_customer=False)
