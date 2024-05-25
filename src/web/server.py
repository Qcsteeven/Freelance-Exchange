from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
from urllib.parse import urlparse
from typing import Any
import json
import cgi
from web.exceptions import ResponseException, BadRequest
from web.routes.interface import SimpleRoute, RegexpRoute
from web.controllers import ResponseHTML, ResponseJSON


class Web(BaseHTTPRequestHandler):
    _simple_routes: dict[str, SimpleRoute]
    _regexp_routes: list[RegexpRoute]

    def __init__(self, simple_routes: dict[str, SimpleRoute], regexp_routes: list[RegexpRoute], *args, **kwargs):
        self._simple_routes = simple_routes
        self._regexp_routes = regexp_routes
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
        # pylint: disable=broad-exception-caught
        except Exception as e:
            print(e)
            self.handle_error(e)

    def try_handle_request(self, method: str):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        #query_params = parse_qs(parsed_url.query)
        response: None | ResponseHTML | ResponseJSON = None

        # Simple Route
        if path in self._simple_routes and method in self._simple_routes[path].methods:
            response = self._simple_routes[path].handle(self, method)

        # Regexp Route
        if response is None:
            for route in self._regexp_routes:
                if method in route.methods:
                    match = route.regexp.match(path)
                    if not match is None:
                        response = route.handle(self, match, method)

        # error 404
        if response is None:
            raise BadRequest()

        self.send_from_controller_response(response)

    def get_body(self) -> dict[str, Any] | None:
        try:
            return self.try_get_body()
        except Exception as e:
            raise BadRequest() from e

    def try_get_body(self) -> dict[str, Any] | None:
        content_type = self.headers.get('Content-Type')

        if content_type:
            if content_type.startswith('application/json'):
                body = self.get_raw_body()
                return json.loads(body)
            elif content_type.startswith('multipart/form-data'):

                parsed_body = self.parse_multipart_form_data()
                return parsed_body
        return None

    def get_raw_body(self) -> str:
        content_length = int(self.headers.get('Content-Length', 0))
        return self.rfile.read(content_length).decode()

    def parse_multipart_form_data(self) -> dict[str, Any]:
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})
        parsed_body = {}

        # pylint: disable=consider-using-dict-items
        for field in form.keys():
            if isinstance(form[field], cgi.FieldStorage):
                parsed_body[field] = form[field].file.read()
            else:
                parsed_body[field] = form[field].value
        return parsed_body

    def handle_error(self, error: Exception):
        if isinstance(error, ResponseException):
            self.send_error(error.code, error.message)
        else:
            self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR)

    def send_from_controller_response(self, response: ResponseHTML | ResponseJSON):
        self.send_response(response.code)
        self.send_header('Content-Type', response.type)
        self.end_headers()

        if isinstance(response, ResponseHTML):
            self.wfile.write(response.body.encode())
        elif isinstance(response, ResponseJSON):
            self.wfile.write(json.dumps(response.body).encode())

def start_server(simple_routes: dict[str, SimpleRoute], regexp_routes: list[RegexpRoute], server_port: int):
    server_address = ('localhost', server_port)
    init_web = lambda *args, **kwargs: Web(simple_routes, regexp_routes, *args, **kwargs)
    server = HTTPServer(server_address, init_web)
    server.serve_forever()
