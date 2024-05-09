from pydantic import BaseModel
from datetime import datetime
from .user import User

class Company(BaseModel):
    id: int
    customer: User
    performer: User
    status: str
    description: str
    create_date: datetime
    start_date: datetime | None
    close_date: datetime | None
    category: str
    description: str
    technology_stack: list[str]