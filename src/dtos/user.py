from pydantic import BaseModel
from .customer import CustomerProfile
from .performer import PerformerProfile

class User(BaseModel):
    id: int
    profiles: CustomerProfile | PerformerProfile 
    is_customer: bool
