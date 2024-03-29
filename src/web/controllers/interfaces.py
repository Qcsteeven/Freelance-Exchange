from dataclasses import dataclass
from enum import Enum

class ResponseType(Enum):
    HTML = 'text/html'
    JSON = 'application/json'

@dataclass
class Response:
    type: ResponseType
    body: str
    status_code: int
