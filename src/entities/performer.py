from dataclasses import dataclass
from rating import Rating
from order import Order
from base import DataBaseStatus

@dataclass
class PerformerOptions:
    firstName: str
    secondName: str | None


class Performer:
    _db_status: DataBaseStatus
    _id: int | None
    _mail: str | None
    _telephone: str | None
    _first_name: str
    _second_name: str | None
    _skills: list[str]
    _rating: Rating
    def __init__(self):
        pass

    def create(self, options: PerformerOptions):
        self._first_name = options.firstName
        self._second_name = options.secondName
        self._db_status = DataBaseStatus.NEW

    def get_rating(self) -> Rating:
        pass

    def get_active_orders(self) -> list[Order]:
        pass

    def request(self, order: Order):
        pass

    def delete(self):
        pass
