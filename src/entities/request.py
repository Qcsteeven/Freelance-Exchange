from typing import TypeVar, Generic
from .performer import Performer


OrderClone = TypeVar('OrderClone')


class Request(Generic[OrderClone]):
    _id: int | None
    _performer: int | Performer
    _order: int | OrderClone


    def __init__(self, order: OrderClone):
        pass
