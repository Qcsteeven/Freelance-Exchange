from dataclasses import dataclass
from .company import Company
from .order import Order
from .base import DataBaseStatus
from typing import Callable, Any


@dataclass
class CustomerOptions:
    first_name: str
    second_name: str


class Customer:
    _db_status: DataBaseStatus
    _id: int | None
    _mail: str | None
    _telephone: str | None
    _first_name: str
    _second_name: str | None
    _company: Company | None
    save: Callable[[Any]]

    def __init__(self):
        pass

    def create(self, options: CustomerOptions):
        self._first_name = options.first_name
        self._second_name = options.second_name
        self._db_status = DataBaseStatus.NEW
        self.save(self)

    def get_company(self) -> Company:
        self._db_status = DataBaseStatus.STATIC
        self.save(self)
        return self._company

    def get_orders(self) -> list[Order]:
        self._db_status = DataBaseStatus.STATIC
        self.save(self)
        return []

    def change_company(self, company: Company):
        self._company = company
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def change_mail(self, mail: str):
        self._mail = mail
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def change_telephone(self, telephone: str):
        self._telephone = telephone
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def change_first_name(self, first_name: str):
        self._first_name = first_name
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def change_second_name(self, second_name: str):
        self._second_name = second_name
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)
