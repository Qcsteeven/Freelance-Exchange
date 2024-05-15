from dataclasses import dataclass
from datetime import datetime
from multipledispatch import dispatch
from typing import TypeVar, Generic

OrderClone = TypeVar('OrderClone')
CustomerClone = TypeVar('CustomerClone')
PerformerClone = TypeVar('PerformerClone')

@dataclass
class Message:
    value: str
    date: datetime
    readed: bool
    _chat: int
    _owner: int


class Chat(Generic[OrderClone, CustomerClone, PerformerClone]):
    _id: int | None
    _message: str

    def __init__(self, order: OrderClone, cus: CustomerClone, per: PerformerClone):
        pass

    def get_order(self) -> OrderClone:
        pass

    def get_messages(self) -> list[Message]:
        pass

    def get_customer(self) -> CustomerClone:
        pass

    def get_performer(self) -> PerformerClone:
        pass

    @dispatch(PerformerClone, Message)
    def send_message(self, per: PerformerClone, msg: Message):
        pass

    @dispatch(CustomerClone, Message)
    def send_message(self, cus: CustomerClone, msg: Message):
        pass
