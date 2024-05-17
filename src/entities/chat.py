from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar, Generic, Any, Callable, Type
from .base import DataBaseStatus


OrderClone = TypeVar('OrderClone')
CustomerClone = TypeVar('CustomerClone')
PerformerClone = TypeVar('PerformerClone')


@dataclass
class Message:
    value: str
    date: datetime
    readed: bool
    chat: int
    owner: int

@dataclass
class SMChat:
    id: int | None
    message: str
    order: OrderClone
    customer: CustomerClone
    performer: PerformerClone
    messages: list[Message]


class Chat(Generic[OrderClone, CustomerClone, PerformerClone]):
    _db_status: DataBaseStatus
    _id: int | None
    _message: str
    _order: OrderClone
    _customer: CustomerClone
    _performer: PerformerClone
    _messages: list[Message]
    save: Callable[[Any]]

    def __init__(self, order: Type[OrderClone], cus: Type[CustomerClone], per: Type[PerformerClone]):
        pass

    def create(self, chat: SMChat):
        self.make(chat)
        self._db_status = DataBaseStatus.NEW
        self.save(self)
        self._db_status = DataBaseStatus.STATIC

    def make(self, chat: SMChat):
        self._id = chat.id
        self._message = chat.message
        self._order = chat.order
        self._customer = chat.customer
        self._performer = chat.performer
        self._messages = chat.messages

    def get_order(self) -> OrderClone:
        return self._order

    def get_messages(self) -> list[Message]:
        return self._messages

    def get_customer(self) -> CustomerClone:
        return self._customer

    def get_performer(self) -> PerformerClone:
        return self._performer

    def send_message(self, user: PerformerClone | CustomerClone, msg: Message):
        msg.owner = user
        self._messages.append(msg)
        self._db_status = DataBaseStatus.UPDATED

    def get_db_status(self) -> DataBaseStatus:
        return self._db_status

    def set_db_status(self, status: DataBaseStatus):
        self._db_status = status
