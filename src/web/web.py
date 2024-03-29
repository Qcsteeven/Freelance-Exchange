from http.server import HTTPServer, BaseHTTPRequestHandler
from http.client import HTTPException
from urllib.parse import urlparse#, parse_qs
from controllers.types import Response
from http import HTTPStatus
from patches import patches
import json

class Web(BaseHTTPRequestHandler):
    def do_GET(self):
        handle_request('GET')

    def do_POST(self):
        handle_request('POST')
    
    def do_PUT(self):
        handle_request('PUT')
    
    def do_DELETE(self):
        handle_request('DELETE')
    
    def handle_request(self, method: str):
        try:
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            #query_params = parse_qs(parsed_url.query)
            response = None

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

            if response == None:
                response = Response(type='http', body="", status_code=HTTPStatus.NOT_FOUND)

            self.send_from_controller_response(response)
        except HTTPException as e:
            self.handle_error(e)

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
