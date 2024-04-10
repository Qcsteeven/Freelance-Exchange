from dataclasses import dataclass
from typing import Any

@dataclass
class Response:
    body: Any
    type: str = ''
    code: int = 200

@dataclass
class ResponseHTML(Response):
    body: str
    type = 'text/html'
    code: int = 200

@dataclass
class ResponseJSON:
    body: dict | tuple | list | int | str
    type = 'application/json'
    code: int = 200
