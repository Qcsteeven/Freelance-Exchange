from dataclasses import dataclass
from typing import TypeVar, Generic, Callable, Any
from .base import DataBaseStatus


CustomerClone = TypeVar('CustomerClone')


@dataclass
class CompanyOptions:
    name: str


class Company(Generic[CustomerClone]):
    _db_status: DataBaseStatus
    _id: int | None
    _mail: str | None
    _telephone: str | None
    _name: str
    _description: str | None
    _customer: CustomerClone
    save: Callable[[Any]]

    def __init__(self, cus: CustomerClone):
        pass

    def create(self, options: CompanyOptions):
        self._name = options.name
        self._db_status = DataBaseStatus.NEW
        self.save(self)

    def delete(self):
        self._db_status = DataBaseStatus.DELETE
        self.save(self)

    def get_customer(self) -> CustomerClone:
        self._db_status = DataBaseStatus.STATIC
        self.save(self)
        return self._customer

    def change_name(self, name: str):
        self._name = name
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

    def change_description(self, description: str):
        self._description = description
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)
