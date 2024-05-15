from typing import TypedDict, Any
from datetime import datetime
from psycopg import Connection
from .table import Table

class SessionInfo(TypedDict):
    owner: int
    create_date: float | None
    key: str

class SessionInfoTransformed(TypedDict):
    owner: int
    create_date: float
    key: str

class SessionRow(TypedDict):
    owner: int
    create_date: float
    key: str

class SessionsTable(Table[SessionInfo, SessionInfoTransformed, SessionRow]):
    table = 'sessions'
    _properties = ['owner', 'create_date']
    _id = 'id'

    def _insert_before(self, con: Connection, info: SessionInfo) -> SessionInfoTransformed:
        create_date = info['create_date']
        if create_date is None:
            create_date = datetime.now().timestamp()

        return SessionInfoTransformed(
            owner=info['owner'],
            create_date=create_date,
            key=info['key']
        )

    def _update_before(self, con: Connection, identifier: int, info: SessionInfo) -> SessionInfoTransformed:
        create_date = info['create_date']
        if create_date is None:
            create_date = datetime.now().timestamp()

        return SessionInfoTransformed(
            owner=info['owner'],
            create_date=create_date,
            key=info['key']
        )

    def _get_values(self, info: SessionInfoTransformed) -> list[Any]:
        return [info['owner'], info['create_date'], info['key']]

    def _get_zero_row(self) -> SessionInfoTransformed:
        return SessionInfoTransformed(owner=0, create_date=0.0, key='')
