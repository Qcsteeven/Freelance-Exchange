from dataclasses import dataclass
from rating import Rating
from company import Company
from order import Order
from base import DataBaseStatus

@dataclass
class CustomerOptions:
    firstName: str
    secondName: str


class Customer:
    _db_status: DataBaseStatus
    _id: int | None
    _mail: str | None
    _telephone: str | None
    _first_name: str
    _second_name: str | None
    _company: Company | None
    _rating: Rating
    def __init__(self):
        pass

    def create(self, options: CustomerOptions):
        self._first_name = options.firstName
        self._second_name = options.secondName
        self._db_status = DataBaseStatus.NEW

    def get_rating(self) -> Rating:
        pass

    def get_company(self) -> Company:
        pass

    def get_orders(self) -> list[Order]:
        pass

    def change_company(self, company: Company):
        pass

    # TODO: Create "change" methods
