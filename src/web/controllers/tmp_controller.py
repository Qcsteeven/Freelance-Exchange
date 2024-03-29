from http import HTTPStatus
from .interfaces import Response, ResponseType


class TmpController:

    def __init__(self):
        pass

    def tmp_method(self, body: str = 'TmpController().tmp_method()') -> Response:
        return Response(type=ResponseType.HTML, body=body, status_code=HTTPStatus.OK)
