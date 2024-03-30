from performer import Performer
from order import Order


class Request:
    _id: int | None
    _performer: int | Performer
    _order: int | Order


    def __init__(self):
        pass
