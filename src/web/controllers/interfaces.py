from dataclasses import dataclass

@dataclass
class Response:
    type: str
    body: str
    status_code: int
