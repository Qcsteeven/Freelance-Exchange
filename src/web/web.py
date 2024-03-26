from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPRequestHandler(BaseHTTPRequestHandler):
    # Обработчик GET-запросов
    def do_GET(self):
        # Ответ сервера
        self.send_response(200)  # Код ответа 200 OK
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Тело ответа
        self.wfile.write(b"Hello, world!")  # Отправляем "Hello, world!" клиенту

# Создание HTTP-сервера и указание порта
def run():
    server_address = ('', 8000)  # Пустая строка означает использование localhost
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    # Запуск сервера
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
