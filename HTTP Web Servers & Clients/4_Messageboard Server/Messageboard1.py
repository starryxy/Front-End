#!/usr/bin/env python3
#
# Use a GET request to display the messageboard's existing contents,
# and POST to update the contents by creating new messages
#
# Why don't we want to use GET for submitting the form?
# Imagine if a user did this. They write a message and press the submit button...
# and the message text shows up in their URL bar. If they press reload, it sends
# the message again. If they bookmark that URL and go back to it, it sends the
# message again. This doesn't seem like such a great experience.
#
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
#
# To test, run this server and test it from your browser using the
# Messageboard.html form, submit message. Then run the test1.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

# from urllib.parse import urlparse, parse_qs
# address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
# parts = urlparse(address)
# print(parts)
# # ParseResult(scheme='https', netloc='www.google.com', path='/search', params='', query='q=gray+squirrel&tbm=isch', fragment='')
#
# print(parts.query)
# # q=gray+squirrel&tbm=isch
#
# query = parse_qs(parts.query)
# query
# # dict of list
# # {'q': ['gray squirrel'], 'tbm': ['isch']}

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Use Content-Length header to get length of the message
        length = int(self.headers.get('Content-length', 0))
        # Read the correct amount of data from the request
        data = self.rfile.read(length).decode()
        # Extract the "message" field from the request data
        for message in parse_qs(data)['message']:
            # Send the "message" field back as the response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
