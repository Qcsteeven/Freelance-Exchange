from http import HTTPStatus
from re import Match, compile as regexp_compile
from .interface import SimpleRoute, RegexpRoute
from .controllers.tmp_controller import TmpController
from .controllers.interfaces import Response, ResponseType
from .pages.tmp import TmpPage
from .server import Web


# Simple Route

class TmpOne(SimpleRoute):
    path = '/tmp-1'
    methods = ['GET']

    # pylint: disable=unused-argument
    def handle(self, req: Web):
        return TmpController().tmp_method()

class TmpTwo(SimpleRoute):
    path = '/tmp-2'
    methods = ['GET', 'POST']

    def handle(self, req: Web):
        return Response(
            type=ResponseType.HTML,
            body=TmpPage().generate(req.path),
            status_code=HTTPStatus.OK
        )

simple_routes_array: list[SimpleRoute] = [TmpOne(), TmpTwo()]
simple_routes: dict[str, SimpleRoute] = {}

for route in simple_routes_array:
    simple_routes[route.path] = route


# Regexp Route
# regexp example
# re.compile(r'^/tmp-match/(?P<something_text>[^/]+)/?$').match('/tmp-match/hello').group('something_text')

class TmpMatch(RegexpRoute):
    regexp = regexp_compile(r'^/tmp-match/(?P<something_text>[^/]+)/?$')
    methods = ['GET', 'POST']

    def handle(self, req: Web, match: Match):
        something_text: str = match.group('something_text')
        body = 'Не робит' # req.get_body()
        return Response(
            type=ResponseType.HTML,
            body=f'path: {req.path}\nmatched: {something_text}\nbody: {body}',
            status_code=HTTPStatus.OK
        )

regexp_routes: list[RegexpRoute] = [TmpMatch()]
