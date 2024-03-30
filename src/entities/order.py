from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from customer import Customer
from request import Request
from company import Company
from chat import Chat
from base import DataBaseStatus

@dataclass
class OrderOptions:
    title: str
    customer: Customer
    descriptions: str

class OrderStatus(Enum):
    ACTIVE = 'ACTIVE'
    PROCESS = 'PROCESS'
    CLOSE = 'CLOSE'

class Order:
    _db_status: DataBaseStatus
    _title: str
    _descriptions: str
    _id: int | None
    _customer: int | Customer
    _performer: int | None
    _status: OrderStatus
    _create: datetime
    _start_process: datetime | None
    _close: datetime | None
    _category: str
    _technology_stack: list[str]
    _chat: Chat | None
    _chats: list[Chat]


    def __init__(self):
        pass

    def create(self, options: OrderOptions):
        self._title = options.title
        self._customer = options.customer
        self._descriptions = options.descriptions
        self._db_status = DataBaseStatus.NEW

    def close(self):
        pass

    def delete(self):
        pass

    def get_all_request(self) -> list[Request]:
        pass

    def select_request(self, req: Request):
        pass

    def get_status(self):
        pass

    def get_customer(self):
        pass

    def get_company(self) -> Company:
        pass

    def change_title(self):
        pass

    def change_description(self):
        pass

    # TODO: Create "change" methods
