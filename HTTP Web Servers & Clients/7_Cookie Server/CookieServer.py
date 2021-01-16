#!/usr/bin/env python3
#
# An HTTP server that remembers your name (in a cookie).
#
# In this exercise, you'll create and read a cookie to remember the name
# that the user submits in a form.

from http.server import HTTPServer, BaseHTTPRequestHandler
from http.cookies import SimpleCookie, CookieError
from urllib.parse import parse_qs
# escape any HTML special characters that might be in the cookie to display the cookie data as HTML
from html import escape as html_escape

form = '''<!DOCTYPE html>
<title>I Remember You</title>
<p>
{}
<p>
<form method="POST">
<label>What's your name again?
<input type="text" name="yourname">
</label>
<br>
<button type="submit">Tell me!</button>
</form>
'''

class NameHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Length of the post data
        length = int(self.headers.get('Content-length', 0))

        # Read and parse the post data
        data = self.rfile.read(length).decode()
        yourname = parse_qs(data)["yourname"][0]

        # Create cookie
        c = SimpleCookie()

        # Set cookie fields: value, domain (localhost), max-age
        c['yourname'] = yourname
        c['yourname']["domain"] = "localhost"
        c['yourname']["max-age"] = 60

        # Send a 303 back to the root page, with a cookie
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.send_header('Set-Cookie', c['yourname'].OutputString())
        self.end_headers()

    def do_GET(self):
        # Default message if we don't know a name
        message = "I don't know you yet!"

        # Look for a cookie in the request
        if 'cookie' in self.headers:
            try:
                # Get the cookie from the headers and extract its value
                in_cookie = SimpleCookie(self.headers["cookie"])
                name = in_cookie["yourname"].value

                # Craft a message, escaping any HTML special chars in name
                message = "Hey there, " + html_escape(name)
            except (KeyError, CookieError) as e:
                message = "I'm not sure who you are!"
                print(e)

        # Send a 200 OK response
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Send the form with the message in it
        mesg = form.format(message)
        self.wfile.write(mesg.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, NameHandler)
    httpd.serve_forever()
