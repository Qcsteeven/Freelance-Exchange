from pydantic import BaseModel
from .user import User
from .order import Order

class Chat(BaseModel):
    id: int
    performer: User
    order_link: Order