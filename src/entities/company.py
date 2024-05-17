from dataclasses import dataclass
from typing import TypeVar, Generic, Callable, Any, Type
from .base import DataBaseStatus


CustomerClone = TypeVar('CustomerClone')


@dataclass
class SMCompany:
    id: int | None
    mail: str | None
    telephone: str | None
    name: str
    description: str | None
    customer: CustomerClone


class Company(Generic[CustomerClone]):
    _db_status: DataBaseStatus
    _id: int | None
    _mail: str | None
    _telephone: str | None
    _name: str
    _description: str | None
    _customer: CustomerClone
    save: Callable[[Any]]

    def __init__(self, cus: Type[CustomerClone]):
        pass

    def create(self, company: SMCompany):
        self.make(company)
        self._db_status = DataBaseStatus.NEW
        self.save(self)
        self._db_status = DataBaseStatus.STATIC

    def make(self, company: SMCompany):
        self._id = company.id
        self._mail = company.mail
        self._telephone =  company.telephone
        self._name =  company.name
        self._description =  company.description
        self._customer =  company.customer

    def delete(self):
        self._db_status = DataBaseStatus.DELETE
        self.save(self)

    def get_customer(self) -> CustomerClone:
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

    def get_db_status(self) -> DataBaseStatus:
        return self._db_status

    def set_db_status(self, status: DataBaseStatus):
        self._db_status = status
