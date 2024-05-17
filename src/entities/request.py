from typing import TypeVar, Generic, Callable, Any, Type
from .performer import Performer
from .base import DataBaseStatus


OrderClone = TypeVar('OrderClone')


class SMRequest:
    id: int | None
    performer: int | Performer
    order: int | OrderClone


class Request(Generic[OrderClone]):
    _db_status: DataBaseStatus
    _id: int | None
    _performer: int | Performer
    _order: int | OrderClone
    save: Callable[[Any]]

    def __init__(self, order: Type[OrderClone]):
        pass

    def create(self, req: SMRequest):
        self.make(req)
        self._db_status = DataBaseStatus.NEW
        self.save(self)
        self._db_status = DataBaseStatus.STATIC

    def make(self, req: SMRequest):
        self._id = req.id
        self._performer = req.performer
        self._order = req.order

    def get_performer(self) -> Performer:
        self.save(self)
        return self._performer

    def set_performer(self, per: Performer):
        self._performer = per
        self._db_status = DataBaseStatus.UPDATED
        self.save(self)

    def delete(self):
        self._db_status = DataBaseStatus.DELETE
        self.save(self)

    def get_db_status(self) -> DataBaseStatus:
        return self._db_status

    def set_db_status(self, status: DataBaseStatus):
        self._db_status = status
