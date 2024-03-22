from dataclasses import dataclass
from rating import Rating
from order import Order


@dataclass
class PerformerOptions:
    firstName: str
    secondName: str


class Performer:
    def __init__(self):
        pass

    def create(self, options: PerformerOptions):
        pass

    def get_rating(self) -> Rating:
        pass

    def get_active_orders(self) -> list[Order]:
        pass

    def request(self, order: Order):
        pass

    def delete(self):
        pass
