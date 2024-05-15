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
        self._db_status = DataBaseStatus.NEW

    def close(self):
        self._status = OrderStatus.CLOSE
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def delete(self):
        self._status = OrderStatus.CLOSE
        self.save(self)

    def get_all_request(self) -> list[Request]:
        self.save(self)

    def select_request(self, req: Request):
        self.save(self)

    def get_status(self):
        self.save(self)

    def get_customer(self):
        self.save(self)

    def get_company(self) -> Company:
        self.save(self)

    def change_title(self):
        self.save(self)

    def change_description(self):
        self.save(self)
