#!/usr/bin/env python3
#
# PRG (Post-Redirect-Get) pattern is a very common design pattern for interactive
# HTTP applications and APIs. A client POSTs to a server to create or update a resource;
# on success, the server replies with a 303 redirect instead of a 200 OK.
# The redirect causes the client to GET the created or updated resource.
#
# For the messageboard server, Post-Redirect-Get means:
#
# 1. You go to http://localhost:8000/ in your browser.
#     Your browser sends a GET request to the server, which replies with a 200 OK and a piece of HTML.
#     You see a form for posting comments, and a list of the existing comments.
#     (But at the beginning, there are no comments posted yet.)
# 2. You write a comment in the form and submit it.
#     Your browser sends it via POST to the server.
# 3. The server updates the list of comments, adding your comment to the list.
#     Then it replies with a 303 redirect, setting the Location: / header to tell the browser to request the main page via GET.
# 4. The redirect response causes your browser to go back to the same page you started with, sending a GET request, which replies with a 200 OK and a piece of HTML.
#
# One big advantage of Post-Redirect-Get is that as a user, every page you actually see
# is the result of a GET request, which means you can bookmark it, reload it, etc.
# — without ever accidentally resubmitting a form.
#
#
# Step three in building the messageboard server. Run the test3.py script to check it.


from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

memory = []

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Use Content-Length header to get length of the message
        length = int(self.headers.get('Content-length', 0))

        # Read the correct amount of data from the request
        data = self.rfile.read(length).decode()
        # Extract the "message" field from the request data
        message = parse_qs(data)["message"][0]

        # Replace HTML tag < with entity name in the message
        message = message.replace("<", "&lt;")

        # Store it in memory
        memory.append(message)

        # Send a 303 redirect via GET back to the root page
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()


    def do_GET(self):
        # send a 200 OK response
        self.send_response(200)

        # send headers
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Put the response together combining the form and the stored messages
        response = form.format("\n".join(memory))

        # send the response
        self.wfile.write(response.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
