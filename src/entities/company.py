from dataclasses import dataclass
from customer import Customer
from base import DataBaseStatus

@dataclass
class CompanyOptions:
    name: str


class Company:
    _db_status: DataBaseStatus
    _id: int | None
    _mail: str | None
    _telephone: str | None
    _name: str
    _description: str | None
    def __init__(self):
        pass

    def create(self, options: CompanyOptions):
        self._name = options.name
        self._db_status = DataBaseStatus.NEW

    def delete(self):
        pass

    def get_customer(self) -> Customer:
        pass

    # TODO: Create "change" methods
