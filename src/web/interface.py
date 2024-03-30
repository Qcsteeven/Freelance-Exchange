from typing import TypeVar, Generic
from re import Match, Pattern
from abc import ABC, abstractmethod
from .controllers.interfaces import Response


Request = TypeVar('Request')

class SimpleRoute(ABC, Generic[Request]):
    path: str
    methods: list[str]

    @abstractmethod
    def handle(self, req: Request) -> Response:
        pass

class RegexpRoute(ABC, Generic[Request]):
    regexp: Pattern
    methods: list[str]

    @abstractmethod
    def handle(self, req: Request, match: Match) -> Response:
        pass
