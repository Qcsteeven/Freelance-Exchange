from pydantic import BaseModel

class Contact(BaseModel):
    id: int
    email: str | None
    telephone: str | None
