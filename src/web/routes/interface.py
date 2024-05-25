from typing import TypeVar, Generic
from re import Match, Pattern
from abc import ABC, abstractmethod
from web.controllers import ResponseHTML, ResponseJSON


Request = TypeVar('Request')

class SimpleRoute(ABC, Generic[Request]):
    path: str
    methods: list[str]

    @abstractmethod
    def handle(self, req: Request, method: str) -> ResponseHTML | ResponseJSON:
        pass

class RegexpRoute(ABC, Generic[Request]):
    regexp: Pattern
    methods: list[str]

    @abstractmethod
    def handle(self, req: Request, match: Match, method: str) -> ResponseHTML | ResponseJSON:
        pass
