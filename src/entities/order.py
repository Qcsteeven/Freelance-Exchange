from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from typing import TypeVar, Generic, Any, Callable
from .request import Request
from .company import Company
from .chat import Chat
from .base import DataBaseStatus


CustomerClone = TypeVar('CustomerClone')


@dataclass
class OrderOptions:
    title: str
    customer: CustomerClone
    descriptions: str

class OrderStatus(Enum):
    ACTIVE = 'ACTIVE'
    PROCESS = 'PROCESS'
    CLOSE = 'CLOSE'
    DELETE = 'DELETE'

class Order(Generic[CustomerClone]):
    _db_status: DataBaseStatus
    _title: str
    _descriptions: str
    _id: int | None
    _customer: int | CustomerClone
    _performer: int | None
    _status: OrderStatus
    _create: datetime
    _start_process: datetime | None
    _close: datetime | None
    _category: str
    _technology_stack: list[str]
    _chat: Chat | None
    _chats: list[Chat]
    save: Callable[[Any]]


    def __init__(self, cus : CustomerClone):
        pass

    def create(self, options: OrderOptions):
        self._title = options.title
        self._customer = options.customer
        self._descriptions = options.descriptions
        self._technology_stack = list[str]
        self._create = datetime
        self._db_status = DataBaseStatus.NEW
        self.save(self)

    def close(self):
        self._close = datetime
        self._status = OrderStatus.CLOSE
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def delete(self):
        self._status = OrderStatus.DELETE
        self._db_status = DataBaseStatus.DELETE
        self.save(self)

    def get_all_request(self) -> list[Request]:
        self._db_status = DataBaseStatus.STATIC
        self.save(self)
        return []

    def select_request(self, req: Request):
        self._performer = req.get_performer()
        self._start_process = datetime
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def get_status(self) -> OrderStatus:
        self.save(self)
        self._db_status = DataBaseStatus.STATIC
        return self._status

    def get_customer(self) -> CustomerClone:
        self.save(self)
        self._db_status = DataBaseStatus.STATIC
        return self._customer

    def get_company(self) -> Company:
        self.save(self)
        self._db_status = DataBaseStatus.STATIC
        return self._customer.get_company()

    def change_title(self, title: str):
        self._title = title
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def change_description(self, description: str):
        self._descriptions = description
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)
