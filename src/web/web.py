from http.server import HTTPServer, BaseHTTPRequestHandler
from http.client import HTTPException
from urllib.parse import urlparse#, parse_qs
from response import Response
from http import HTTPStatus
from patches import patches
import json

class Web(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            parsed_url = urlparse(self.path)
            #path = parsed_url.path
            #query_params = parse_qs(parsed_url.query)
            if parsed_url.path in patches:
                response = Response(type='http', body=patches[parsed_url.path], status_code=HTTPStatus.OK)
            else:
                response = Response(type='http', body="", status_code=HTTPStatus.NOT_FOUND)
            self.send_from_controller_response(response)
        except HTTPException as e:
            self.handle_error(e)

    def do_POST(self):
        try:
            response = Response(type='http', body="Hello, POST!", status_code=HTTPStatus.OK)
            self.send_from_controller_response(response)
        except HTTPException as e:
            self.handle_error(e)
    
    def do_PUT(self):
        try:
            response = Response(type='http', body="Hello, PUT!", status_code=HTTPStatus.OK)
            self.send_from_controller_response(response)
        except HTTPException as e:
            self.handle_error(e)
    
    def do_DELETE(self):
        try:
            response = Response(type='http', body="Hello, DELETE!", status_code=HTTPStatus.OK)
            self.send_from_controller_response(response)
        except HTTPException as e:
            self.handle_error(e)
        
    def handle_error(self, error):
        if isinstance(error, ValueError):
            self.send_error(HTTPStatus.BAD_REQUEST)
        else:
            self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR)
        
    def send_from_controller_response(self, response):
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

def run():
    server = HTTPServer(('localhost', 5000), Web)
    server.serve_forever()

if __name__ == '__main__':
    run()
