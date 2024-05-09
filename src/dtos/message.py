from pydantic import BaseModel
from .user import User
from .chat import Chat
from datetime import datetime

class Message(BaseModel):
    id: int
    chat: Chat
    owner: User
    date: datetime
    value: str