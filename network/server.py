import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.end_headers()

    def _replay(self, message):
        return message.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._replay("Hello, otus!"))


def run(server_class=HTTPServer, handler_class=Server, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


parser = argparse.ArgumentParser(description="Run a simple HTTP server")
parser.add_argument(
    "-l",
    "--listen",
    default="localhost",
    help="Specify the IP address on which the server listens",
)
parser.add_argument(
    "-p",
    "--port",
    type=int,
    default=8000,
    help="Specify the port on which the server listens",
)
args = parser.parse_args()
run(addr=args.listen, port=args.port)
