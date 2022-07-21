from http.server import HTTPServer, BaseHTTPRequestHandler
from send_in_database import send_request

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # определяем метод `do_GET`
    def do_GET(self):
        if self.path.endswith("/get"):
            self.send_response(200)
            self.end_headers()
            self.wfile.write('Hello, get!'.encode())


    def do_POST(self):
        '''Reads post request body'''
        if self.path.endswith("/post"):
            self.send_response(200)
            self.end_headers()
            self.wfile.write('Hello, post!'.encode())
            print(self.rfile.read().decode())
            send_request(self.rfile.read().decode())

httpd = HTTPServer(('192.168.0.34', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()