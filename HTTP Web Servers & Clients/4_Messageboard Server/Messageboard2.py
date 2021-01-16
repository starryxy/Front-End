#!/usr/bin/env python3
#
# Step two in building the messageboard server:
# A server that handles both GET and POST requests.
#
# To test, run this server and access it at http://localhost:8000/
# in your browser. You should see the form. Then put a message into the
# form and submit it. You should then see the message echoed back to you.
# Run the test2.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Use Content-Length header to get length of the message
        length = int(self.headers.get('Content-length', 0))

        # Read the correct amount of data from the request
        data = self.rfile.read(length).decode()

        # Extract the "message" field from the request data
        message = parse_qs(data)["message"][0]

        # Send the "message" field back as the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())

    def do_GET(self):
        # send a 200 OK response
        self.send_response(200)

        # send headers
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # response body, encode and send the form
        self.wfile.write(form.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
