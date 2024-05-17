from dataclasses import dataclass
from typing import Callable, Any
from .order import Order
from .base import DataBaseStatus


@dataclass
class SMPerformer:
    id: int | None
    mail: str | None
    telephone: str | None
    first_name: str
    second_name: str | None
    skills: list[str]


class Performer:
    _db_status: DataBaseStatus = DataBaseStatus.STATIC
    _id: int | None
    _mail: str | None
    _telephone: str | None
    _first_name: str
    _second_name: str | None
    _skills: list[str]
    save: Callable[[Any]]
    create_request: Callable[[Any, Order]]
    orders: Callable[[Any]]

    def __init__(self):
        pass

    def create(self, per: SMPerformer):
        self.make(per)
        self._db_status = DataBaseStatus.NEW
        self.save(self)
        self._db_status = DataBaseStatus.STATIC

    def make(self, per: SMPerformer):
        self._id = per.id
        self._mail = per.mail
        self._telephone = per.telephone
        self._first_name = per.first_name
        self._second_name = per.second_name
        self._skills = per.skills

    def get_active_orders(self) -> list[Order]:
        return self.orders(self)

    def request(self, order: Order):
        self.create_request(self, order)

    def delete(self):
        self._db_status = DataBaseStatus.DELETE
        self.save(self)

    def get_db_status(self) -> DataBaseStatus:
        return self._db_status

    def set_db_status(self, status: DataBaseStatus):
        self._db_status = status
