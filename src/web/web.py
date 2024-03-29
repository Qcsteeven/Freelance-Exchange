from http.server import HTTPServer, BaseHTTPRequestHandler
from http.client import HTTPException
from http import HTTPStatus
from typing import Callable
from urllib.parse import urlparse
import json
from .controllers.interfaces import Response, ResponseType


class Web(BaseHTTPRequestHandler):

    _simple_routes: Callable[[any], Response]

    def __init__(self, simple_routes: Callable[[any], Response], *args, **kwargs):
        self._simple_routes = simple_routes
        super().__init__(*args, **kwargs)

    # pylint: disable=invalid-name
    def do_GET(self):
        self.handle_request('GET')

    # pylint: disable=invalid-name
    def do_POST(self):
        self.handle_request('POST')

    # pylint: disable=invalid-name
    def do_PUT(self):
        self.handle_request('PUT')

    # pylint: disable=invalid-name
    def do_DELETE(self):
        self.handle_request('DELETE')

    def handle_request(self, method: str):
        try:
            self.try_handle_request(method)
        except HTTPException as e:
            self.handle_error(e)

    def try_handle_request(self, method: str):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        #query_params = parse_qs(parsed_url.query)
        response: None = None

        if method == 'GET' and path in self._simple_routes:
            response = self._simple_routes[path](self)

        # if response == None:
        #     for route in routes:
        #         if route.method == method:
        #         # {
        #         #     method: str
        #         #     regexp: regexp
        #         #     handle: (self, groups) => Response
        #         # }
        #             result = route.regexp.test(path)
        #             if result:
        #                 route.handle(result.groups)

        if response is None:
            response = Response(type=ResponseType.HTML, body="", status_code=HTTPStatus.NOT_FOUND)

        self.send_from_controller_response(response)

    def handle_error(self, error):
        if isinstance(error, ValueError):
            self.send_error(HTTPStatus.BAD_REQUEST)
        else:
            self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR)

    def send_from_controller_response(self, response: Response):
        self.send_response(response.status_code)

        if response.type == ResponseType.HTML:
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(response.body.encode())
        elif response.type == ResponseType.JSON:
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response.body).encode())

def start_server(simple_routes: Callable[[Web], Response], server_port: int):
    server_address = ('localhost', server_port)
    init_web = lambda *args, **kwargs: Web(simple_routes, *args, **kwargs)
    server = HTTPServer(server_address, init_web)
    server.serve_forever()
