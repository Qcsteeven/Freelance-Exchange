from http import HTTPStatus
from re import Match, compile as regexp_compile
from web.controllers import Response, ResponseType
from web.server import Web
from .interface import RegexpRoute


# regexp example
# re.compile(r'^/tmp-match/(?P<something_text>[^/]+)/?$').match('/tmp-match/hello').group('something_text')

class TmpMatch(RegexpRoute):
    regexp = regexp_compile(r'^/tmp-match/(?P<something_text>[^/]+)/?$')
    methods = ['GET', 'POST']

    def handle(self, req: Web, match: Match):
        something_text: str = match.group('something_text')
        body = req.get_body()
        return Response(
            type=ResponseType.HTML,
            body=f'path: {req.path}\nmatched: {something_text}\nbody: {body}',
            status_code=HTTPStatus.OK
        )
