from typing import TypedDict, Any
from psycopg import Connection
from .table import Table

class RequestInfo(TypedDict):
    performer: int
    order_link: int

class RequestInfoTransformed(TypedDict):
    performer: int
    order_link: int

class RequestRow(TypedDict):
    performer: int
    order_link: int

class RequestsTable(Table[RequestInfo, RequestInfoTransformed, RequestRow]):
    table = 'requests'
    _properties = ['performer', 'order_link']
    _id = 'id'

    def _insert_before(self, con: Connection, info: RequestInfo) -> RequestInfoTransformed:
        return RequestInfoTransformed(
            performer=info['performer'],
            order_link=info['order_link']
        )

    def _update_before(self, con: Connection, identifier: int, info: RequestInfo) -> RequestInfoTransformed:
        return RequestInfoTransformed(
            performer=info['performer'],
            order_link=info['order_link']
        )

    def _get_values(self, info: RequestInfoTransformed) -> list[Any]:
        return [info['performer'], info['order_link']]

    def _get_zero_row(self) -> RequestInfoTransformed:
        return RequestInfoTransformed(performer=0, order_link=0)
