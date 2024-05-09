from pydantic import BaseModel
from .user import User
from .contacts import Contact

class Company(BaseModel):
    id: int
    owner: User
    contacts: Contact
    name: str
    description: str
