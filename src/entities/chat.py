from dataclasses import dataclass
from datetime import datetime
from multipledispatch import dispatch
from customer import Customer
from performer import Performer
from order import Order


@dataclass
class Message:
    value: str
    date: datetime
    readed: bool
    _chat: int
    _owner: int


class Chat:
    _id: int | None
    _message: str

    def __init__(self):
        pass

    def get_order(self) -> Order:
        pass

    def get_messages(self) -> list[Message]:
        pass

    def get_customer(self) -> Customer:
        pass

    def get_performer(self) -> Performer:
        pass

    @dispatch(Performer, Message)
    def send_message(self, per: Performer, msg: Message):
        pass

    @dispatch(Customer, Message)
    def send_message(self, cus: Customer, msg: Message):
        pass
