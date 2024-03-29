from interfaces import Response


class TmpController:

    def __init__(self):
        pass

    def tmp_method(self, body: str = 'TmpController().tmp_method()') -> Response:
        return Response(type='http', body=body, status_code=200)
