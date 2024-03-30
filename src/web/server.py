from http.server import HTTPServer, BaseHTTPRequestHandler
from http.client import HTTPException
from http import HTTPStatus
from typing import Optional, Dict, Any
from urllib.parse import urlparse
import json
import cgi
from .interface import SimpleRoute, RegexpRoute
from .controllers.interfaces import Response, ResponseType


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
        except HTTPException as e:
            self.handle_error(e)

    def try_handle_request(self, method: str):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        #query_params = parse_qs(parsed_url.query)
        response: None | Response = None

        # Simple Route
        if path in self._simple_routes and method in self._simple_routes[path].methods:
            response = self._simple_routes[path].handle(self)

        # Regexp Route
        if response is None:
            for route in self._regexp_routes:
                if method in route.methods:
                    result = route.regexp.match(path)
                    if not result is None:
                        response = route.handle(self, result)

        # error 404
        if response is None:
            response = Response(type=ResponseType.HTML, body="", status_code=HTTPStatus.NOT_FOUND)

        self.send_from_controller_response(response)

    def get_body(self) -> Optional[Dict[str, Any]]:
        try:
            return self.try_get_body()
        except Exception as e:
            raise HTTPException() from e

    def try_get_body(self) -> Optional[Dict[str, Any]]:
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

    def parse_multipart_form_data(self) -> Dict[str, Any]:
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})
        parsed_body = {}

        # pylint: disable=unused-variable
        for field, value in form.items():
            if isinstance(form[field], cgi.FieldStorage):
                parsed_body[field] = form[field].file.read()
            else:
                parsed_body[field] = form[field].value 
        return parsed_body

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

def start_server(simple_routes: dict[str, SimpleRoute], regexp_routes: list[RegexpRoute], server_port: int):
    server_address = ('localhost', server_port)
    init_web = lambda *args, **kwargs: Web(simple_routes, regexp_routes, *args, **kwargs)
    server = HTTPServer(server_address, init_web)
    server.serve_forever()
