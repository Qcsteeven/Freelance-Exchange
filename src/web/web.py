from http.server import HTTPServer, BaseHTTPRequestHandler
from http.client import HTTPException
from http import HTTPStatus
from urllib.parse import urlparse
import json
from controllers.interfaces import Response
from patches import patches


class Web(BaseHTTPRequestHandler):

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

        if method == 'GET' and path in patches:
            response = patches[path](self) # Response(type='http', body=patches[path], status_code=HTTPStatus.OK)

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
            response = Response(type='http', body="", status_code=HTTPStatus.NOT_FOUND)

        self.send_from_controller_response(response)

    def handle_error(self, error):
        if isinstance(error, ValueError):
            self.send_error(HTTPStatus.BAD_REQUEST)
        else:
            self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR)

    def send_from_controller_response(self, response: Response):
        if response.type == 'http':
            self.send_response(response.status_code)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(response.body.encode())
        elif response.type == 'json':
            self.send_response(response.status_code)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response.body).encode())

def start_server(server_port: int):
    server = HTTPServer(('localhost', server_port), Web)
    server.serve_forever()
