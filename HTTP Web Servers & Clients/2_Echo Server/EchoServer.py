#!/usr/bin/env python3
#
# The *echo server* is an HTTP server that responds to a GET request by
# sending the query path back to the client.
# For instance, if you go to the URI "http://localhost:8000/Balloon",
# the echo server will respond with the text "Balloon" in the HTTP response body.
#
# Run the program in your terminal. Try it out from your browser, e.g. open below URIs:
# http://localhost:8000/GoodMorningHTTP
# http://localhost:8000/bears
# http://localhost:8000/spiders_from_mars#stardust
# http://localhost:8000/giant-squid?color=green
# then run the "test.py" script to check.

from http.server import HTTPServer, BaseHTTPRequestHandler


class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # status code
        self.send_response(200)

        # headers
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # response body
        self.wfile.write(self.path[1:].encode())


if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, EchoHandler)
    httpd.serve_forever()
