from dataclasses import dataclass
from typing import Any, Callable
from .company import Company
from .order import Order
from .base import DataBaseStatus


@dataclass
class SMCustomer:
    id: int | None
    mail: str | None
    telephone: str | None
    first_name: str
    second_name: str | None
    company: Company | None

class Customer:
    _db_status: DataBaseStatus = DataBaseStatus.STATIC
    _id: int | None
    _mail: str | None
    _telephone: str | None
    _first_name: str
    _second_name: str | None
    _company: Company | None
    save: Callable[[Any]]
    orders: Callable[[Any]]

    def __init__(self):
        pass

    def create(self, cus: SMCustomer):
        self.make(cus)
        self._db_status = DataBaseStatus.NEW
        self.save(self)
        self._db_status = DataBaseStatus.STATIC

    def make(self, cus: SMCustomer):
        self._id = cus.id
        self._mail = cus.mail
        self._telephone = cus.telephone
        self._first_name = cus.first_name
        self._second_name = cus.second_name
        self._company = cus.company

    def get_company(self) -> Company:
        self.save(self)
        return self._company

    def get_orders(self) -> list[Order]:
        self.save(self)
        return self.orders(self)

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

    def get_db_status(self) -> DataBaseStatus:
        return self._db_status

    def set_db_status(self, status: DataBaseStatus):
        self._db_status = status
