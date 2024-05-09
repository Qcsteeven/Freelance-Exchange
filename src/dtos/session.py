from pydantic import BaseModel
from .user import User

class Session(BaseModel):
    id: int
    owner: User
    key: str