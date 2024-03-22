from dataclasses import dataclass
from customer import Customer


@dataclass
class CompanyOptions:
    title: str


class Company:
    def __init__(self):
        pass

    def create(options: CompanyOptions):
        pass

    def delete(self):
        pass

    def get_customer(self) -> Customer:
        pass

    # TODO: Create "change" methods
