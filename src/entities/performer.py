from dataclasses import dataclass
from .order import Order
from .base import DataBaseStatus
from typing import Callable, Any


@dataclass
class PerformerOptions:
    first_name: str
    second_name: str | None


class Performer:
    _db_status: DataBaseStatus
    _id: int | None
    _mail: str | None
    _telephone: str | None
    _first_name: str
    _second_name: str | None
    _skills: list[str]
    save: Callable[[Any]]

    def __init__(self):
        pass

    def create(self, options: PerformerOptions):
        self._first_name = options.first_name
        self._second_name = options.second_name
        self._db_status = DataBaseStatus.NEW
        self.save(self)

    def get_active_orders(self) -> list[Order]:
        self._db_status = DataBaseStatus.STATIC
        self.save(self)
        return []

    def request(self, order: Order):
        #TODO Отправка запроса на выполнение заказа
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def delete(self):
        self._db_status = DataBaseStatus.DELETE
        self.save(self)
