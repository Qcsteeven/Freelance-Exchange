from pydantic import BaseModel, ValidationError
from typing import Type, Dict
from .contacts import Contact

class CustomerProfile(BaseModel):
    id: int
    contacts: Contact
    first_name: str
    second_name: str | None
    skills: list[str]
