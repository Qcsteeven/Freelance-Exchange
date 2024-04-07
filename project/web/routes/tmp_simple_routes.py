from http import HTTPStatus
from .interface import SimpleRoute
from ..controllers.tmp_controller import TmpController
from ..controllers.interfaces import Response, ResponseType
from ..pages.tmp import TmpPage
from ..server import Web


class TmpOne(SimpleRoute):
    tmp_controller: TmpController
    path = '/tmp-1'
    methods = ['GET']

    def __init__(self, tmp_controller: TmpController):
        self.tmp_controller = tmp_controller

    # pylint: disable=unused-argument
    def handle(self, req: Web):
        return self.tmp_controller.tmp_method()

class TmpTwo(SimpleRoute):
    path = '/tmp-2'
    methods = ['GET', 'POST']

    def handle(self, req: Web):
        return Response(
            type=ResponseType.HTML,
            body=TmpPage().generate(req.path),
            status_code=HTTPStatus.OK
        )

class TmpThree(SimpleRoute):
    path = '/tmp-3'
    methods = ['POST']

    def handle(self, req: Web):
        return Response(
            type=ResponseType.HTML,
            body=TmpPage().generate(req.path),
            status_code=HTTPStatus.OK
        )
