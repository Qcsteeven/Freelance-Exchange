from dataclasses import dataclass
from datetime import datetime
from multipledispatch import dispatch
from typing import TypeVar, Generic
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


class Chat(Generic[OrderClone, CustomerClone, PerformerClone]):
    _db_status: DataBaseStatus
    _id: int | None
    _message: str
    _order: OrderClone
    _customer: CustomerClone
    _performer: PerformerClone
    _messages: list[Message]

    def __init__(self, order: OrderClone, cus: CustomerClone, per: PerformerClone):
        self._db_status = DataBaseStatus.NEW
        self._order = order
        self._customer = cus
        self._performer = per
        self._messages = []

    def get_order(self) -> OrderClone:
        self._db_status = DataBaseStatus.STATIC
        return self._order

    def get_messages(self) -> list[Message]:
        self._db_status = DataBaseStatus.STATIC
        return self._messages

    def get_customer(self) -> CustomerClone:
        self._db_status = DataBaseStatus.STATIC
        return self._customer

    def get_performer(self) -> PerformerClone:
        self._db_status = DataBaseStatus.STATIC
        return self._performer

    @dispatch(PerformerClone, Message)
    def send_message(self, per: PerformerClone, msg: Message):
        msg.owner = per
        self._messages.append(msg)
        self._db_status = DataBaseStatus.UPDATED
        
    @dispatch(CustomerClone, Message)
    def send_message(self, cus: CustomerClone, msg: Message):
        msg.owner = cus
        self._messages.append(msg)
        self._db_status = DataBaseStatus.UPDATED