from typing import TypedDict, Any
from datetime import datetime
from psycopg import Connection
from .table import Table

class RequestInfo(TypedDict):
    owner: int
    create_date: float | None
    key: str

class RequestInfoTransformed(TypedDict):
    owner: int
    create_date: float
    key: str

class RequestRow(TypedDict):
    owner: int
    create_date: float
    key: str

class RequestsTable(Table[RequestInfo, RequestInfoTransformed, RequestRow]):
    table = 'requests'
    _properties = ['owner', 'create_date']
    _id = 'id'

    def _insert_before(self, con: Connection, info: RequestInfo) -> RequestInfoTransformed:
        create_date = info['create_date']
        if create_date is None:
            create_date = datetime.now().timestamp()

        return RequestInfoTransformed(
            owner=info['owner'],
            create_date=create_date,
            key=info['key']
        )

    def _update_before(self, con: Connection, identifier: int, info: RequestInfo) -> RequestInfoTransformed:
        create_date = info['create_date']
        if create_date is None:
            create_date = datetime.now().timestamp()

        return RequestInfoTransformed(
            owner=info['owner'],
            create_date=create_date,
            key=info['key']
        )

    def _get_values(self, info: RequestInfoTransformed) -> list[Any]:
        return [info['owner'], info['create_date'], info['key']]

    def _get_zero_row(self) -> RequestInfoTransformed:
        return RequestInfoTransformed(owner=0, create_date=0.0, key='')
