#!/usr/bin/env python3
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.
# Run this program in your terminal and access the server at
# http://localhost:8000 in your browser.


from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # status code
        self.send_response(200)

        # headers
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # response body
        self.wfile.write("Hello, HTTP!\n".encode())

        # wfile = writeable file
        # self.wfile represents the connection from the server to the client, and is write-only
        # Any binary data written to it with its write method gets sent to the client as part of the response

        # self.wfile.write method in the handler class expects to be given a bytes object
        # — a piece of arbitrary binary data — which it writes over the network in the HTTP response body
        # If want to send a string over the HTTP connection, we need to encode the string into a bytes object
        # The encode method on strings translates the string into a bytes object, which is suitable for sending over the network
        # There is also a decode method for turning bytes objects into strings


if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
