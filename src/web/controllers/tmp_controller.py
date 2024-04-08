from http import HTTPStatus
from storage import Storage
from .interfaces import Response, ResponseType


class TmpController:
    storage: Storage

    def __init__(self, storage: Storage):
        self.storage = storage

    def tmp_method(self, body: str = 'TmpController().tmp_method()') -> Response:
        return Response(type=ResponseType.HTML, body=body, status_code=HTTPStatus.OK)
