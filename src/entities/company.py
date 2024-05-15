from dataclasses import dataclass
from typing import TypeVar, Generic
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
    def __init__(self, cus: CustomerClone):
        pass

    def create(self, options: CompanyOptions):
        self._name = options.name
        self._db_status = DataBaseStatus.NEW

    def delete(self):
        pass

    def get_customer(self) -> CustomerClone:
        pass

    # TODO: Create "change" methods
