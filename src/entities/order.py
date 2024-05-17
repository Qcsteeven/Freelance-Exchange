from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from typing import TypeVar, Generic, Any, Callable, Type
from .request import Request
from .company import Company
from .chat import Chat
from .base import DataBaseStatus


CustomerClone = TypeVar('CustomerClone')


class OrderStatus(Enum):
    ACTIVE = 'ACTIVE'
    PROCESS = 'PROCESS'
    CLOSE = 'CLOSE'
    DELETE = 'DELETE'


@dataclass
class SMOrder:
    title: str
    descriptions: str
    id: int | None
    customer: int | CustomerClone
    performer: int | None
    status: OrderStatus
    create_data: datetime
    start_data: datetime | None
    close_data: datetime | None
    category: str
    technology_stack: list[str]
    chat: Chat | None
    chats: list[Chat]


class Order(Generic[CustomerClone]):
    _db_status: DataBaseStatus = DataBaseStatus.STATIC
    _title: str
    _descriptions: str
    _id: int | None
    _customer: int | CustomerClone
    _performer: int | None
    _status: OrderStatus
    _create_data: datetime
    _start_data: datetime | None = None
    _close_data: datetime | None = None
    _category: str
    _technology_stack: list[str]
    _chat: Chat | None
    _chats: list[Chat]
    save: Callable[[Any]]
    requests: Callable[[Any]]

    def __init__(self, cus: Type[CustomerClone]):
        pass

    def create(self, order: SMOrder):
        self.make(order)
        self._db_status = DataBaseStatus.NEW
        self.save(self)
        self._db_status = DataBaseStatus.STATIC

    def make(self, order: SMOrder):
        self._id = order.id
        self._title = order.title
        self._customer = order.customer
        self._descriptions = order.descriptions
        self._technology_stack = order.technology_stack
        self._create_data = order.create_data
        self._status = OrderStatus.ACTIVE
        self._performer = order.performer
        self._customer = order.customer
        self._category = order.category

    def close(self):
        self._close_data = datetime
        self._status = OrderStatus.CLOSE
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def delete(self):
        self._status = OrderStatus.DELETE
        self._db_status = DataBaseStatus.DELETE
        self.save(self)

    #TODO выпилить
    def get_all_request(self) -> list[Request]:
        self.save(self)
        return self.requests(self)

    def select_request(self, req: Request):
        self._performer = req.get_performer()
        self._start_data = datetime
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def get_status(self) -> OrderStatus:
        self.save(self)
        return self._status

    def get_customer(self) -> CustomerClone:
        self.save(self)
        return self._customer

    def get_company(self) -> Company:
        self.save(self)
        return self._customer.get_company()

    def change_title(self, title: str):
        self._title = title
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def change_description(self, description: str):
        self._descriptions = description
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def get_db_status(self) -> DataBaseStatus:
        return self._db_status

    def set_db_status(self, status: DataBaseStatus):
        self._db_status = status
