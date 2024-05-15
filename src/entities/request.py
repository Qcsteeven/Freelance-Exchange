from typing import TypeVar, Generic
from .performer import Performer
from .base import DataBaseStatus
from typing import Callable, Any


OrderClone = TypeVar('OrderClone')


class Request(Generic[OrderClone]):
    _db_status: DataBaseStatus
    _id: int | None
    _performer: int | Performer
    _order: int | OrderClone
    save: Callable[[Any]]

    def __init__(self, order: OrderClone):
        pass

    def create(self, order: OrderClone, per: Performer):
        self._order = order
        self._performer = Performer
        self._db_status = DataBaseStatus.NEW
        self.save(self)

    def get_performer(self) -> Performer:
        self._db_status = DataBaseStatus.STATIC
        self.save(self)
        return self._performer

    def set_performer(self, per: Performer):
        self._performer = per
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def delete(self):
        self._db_status = DataBaseStatus.DELETE
        self.save(self)
