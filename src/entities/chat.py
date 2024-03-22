from dataclasses import dataclass
from datetime import datetime
from customer import Customer
from performer import Performer
from order import Order


@dataclass
class Message:
    value: str
    date: datetime
    readed: bool


class Chat:
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

    def send_message(self, per: Performer, msg: Message):
        pass

    def send_message(self, cus: Customer, msg: Message):
        pass
