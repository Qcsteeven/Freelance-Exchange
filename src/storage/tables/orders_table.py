from typing import TypedDict, Any
from datetime import datetime, timezone, timedelta
from psycopg import Connection
from .table import Table

class OrderInfo(TypedDict):
    customer: int
    performer: int | None
    status: str
    create_date: str | None
    start_date: str | None
    close_date: str | None
    category: str
    description: str
    technology_stack: list[str]

class OrderInfoTransformed(TypedDict):
    customer: int
    performer: int | None
    status: str
    create_date: str
    start_date: str | None
    close_date: str | None
    category: str
    description: str
    technology_stack: list[str]

class OrderRow(TypedDict):
    customer: int
    performer: int | None
    status: str
    create_date: str
    start_date: str | None
    close_date: str | None
    category: str
    description: str
    technology_stack: list[str]

class OrdersTable(Table[OrderInfo, OrderInfoTransformed, OrderRow]):
    table = 'orders'
    _properties = [
        'customer', 'performer', 'status', 'create_date', 'start_date',
        'close_date', 'category', 'description', 'technology_stack'
    ]
    _id = 'id'

    def _insert_before(self, con: Connection, info: OrderInfo) -> OrderInfoTransformed:
        create_date = info['create_date']
        if create_date is None:
            now = datetime.now(timezone.utc) + timedelta(hours=3)
            create_date = now.strftime('%Y-%m-%d %H:%M:%S+03')

        return OrderInfoTransformed(
            customer=info['customer'],
            performer=info['performer'],
            status=info['status'],
            create_date=create_date,
            start_date=info['start_date'],
            close_date=info['close_date'],
            category=info['category'],
            description=info['description'],
            technology_stack=info['technology_stack']
        )

    def _update_before(self, con: Connection, identifier: int, info: OrderInfo) -> OrderInfoTransformed:
        return OrderInfoTransformed(
            customer=info['customer'],
            performer=info['performer'],
            status=info['status'],
            create_date=info['create_date'],
            start_date=info['start_date'],
            close_date=info['close_date'],
            category=info['category'],
            description=info['description'],
            technology_stack=info['technology_stack']
        )

    def _get_values(self, info: OrderInfoTransformed) -> list[Any]:
        return [
            info['customer'], info['performer'], info['status'], info['create_date'], info['start_date'],
            info['close_date'], info['category'], info['description'], info['technology_stack']
        ]

    def _get_zero_row(self) -> OrderInfoTransformed:
        return OrderInfoTransformed(
            customer=0, performer=None, status='Not Found', create_date=0, start_date=None, close_date=None,
            category='Not Found', description='Not Found', technology_stack=[]
        )
