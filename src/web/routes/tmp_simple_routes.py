from http import HTTPStatus
from web.controllers import TmpController, Response, ResponseType
from web.pages import TmpPage
from web.server import Web
from .interface import SimpleRoute


class TmpOne(SimpleRoute):
    path = '/tmp-1'
    methods = ['GET']
    tmp_controller: TmpController

    def __init__(self, tmp_controller: TmpController):
        self.tmp_controller = tmp_controller

    # pylint: disable=unused-argument
    def handle(self, req: Web):
        return self.tmp_controller.tmp_method()

class TmpTwo(SimpleRoute):
    path = '/tmp-2'
    methods = ['GET', 'POST']
    tmp_page: TmpPage

    def __init__(self, tmp_page: TmpPage):
        self.tmp_page = tmp_page

    def handle(self, req: Web):
        return Response(
            type=ResponseType.HTML,
            body=self.tmp_page.generate(req.path),
            status_code=HTTPStatus.OK
        )

class TmpThree(SimpleRoute):
    path = '/tmp-3'
    methods = ['POST']
    tmp_page: TmpPage

    def __init__(self, tmp_page: TmpPage):
        self.tmp_page = tmp_page

    def handle(self, req: Web):
        return Response(
            type=ResponseType.HTML,
            body=self.tmp_page.generate(req.path),
            status_code=HTTPStatus.OK
        )
