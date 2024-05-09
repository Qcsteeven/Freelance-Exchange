from pydantic import BaseModel
from .contacts import Contact

class PerformerProfile(BaseModel):
    id: int
    contacts: Contact
    first_name: str
    second_name: str | None
    skills: list[str]
