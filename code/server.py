import http.server
import socketserver

PORT = 8000
DIRECTORY = "/server.py"


class Handler(http.server.SimpleHTTPRequestHandler):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, directory=DIRECTORY, **kwargs)


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()