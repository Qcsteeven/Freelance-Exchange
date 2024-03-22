from dataclasses import dataclass
from rating import Rating
from company import Company
from order import Order


@dataclass
class CustomerOptions:
    firstName: str
    secondName: str


class Customer:
    def __init__(self):
        pass

    def create(self, options: CustomerOptions):
        pass

    def get_rating(self) -> Rating:
        pass

    def get_company(self) -> Company:
        pass

    def get_orders(self) -> list[Order]:
        pass

    def change_company(self, company: Company):
        pass

    # TODO: Create "change" methods
