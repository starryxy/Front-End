#!/usr/bin/env python3
#
# A *Bookmark server* or URI shortener that maintains a mapping (dictionary)
# between short names and long URIs, checking that each new URI added to the
# mapping actually works (i.e. returns a 200 OK).
#
# This server is intended to serve three kinds of requests:
#
#   * A GET request to the / (root) path.  The server returns a form allowing
#     the user to submit a new name/URI pairing. The form also includes a
#     listing of all the known pairings.
#   * A POST request containing "longuri" and "shortname" fields.  The server
#     checks that the URI is valid (by requesting it), and if so, stores the
#     mapping from shortname to longuri in its dictionary. The server then
#     redirects back to the root path.
#   * A GET request whose path contains a short name. The server looks up
#     that short name in its dictionary and redirects to the corresponding
#     long URI.
#
#
# After writing each step, restart the server and run test.py to test it.

import http.server
import requests
from urllib.parse import unquote, parse_qs

memory = {}

form = '''<!DOCTYPE html>
<title>Bookmark Server</title>
<form method="POST">
    <label>Long URI:
        <input name="longuri">
    </label>
    <br>
    <label>Short name:
        <input name="shortname">
    </label>
    <br>
    <button type="submit">Save it!</button>
</form>
<p>URIs I know about:
<pre>
{}
</pre>
'''


def CheckURI(uri, timeout=5):
    '''Check whether this URI is reachable, i.e. does it return a 200 OK?
    This function returns True if a GET request to uri returns a 200 OK, and
    False if that GET request returns any other response, or doesn't return
    (i.e. times out).
    '''
    r = requests.get(uri, timeout = timeout)
    if r.status_code == 200:
        return True
    else:
        return False


class Shortener(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # A GET request will either be for / (the root path) or for /some-name.
        # Strip off the / and we have either empty string or a name.
        name = unquote(self.path[1:])

        if name:
            if name in memory:
                # Send a 303 redirect to the long URI in memory[name]
                self.send_response(303)
                self.send_header('Location', memory[name])
                self.end_headers()
            else:
                # Send a 404 error
                self.send_response(404)
                self.send_header('Content-type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write("I don't know '{}'.".format(name).encode())
        else:
            # Show the form at root path
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # List the known associations in the form
            known = "\n".join("{} : {}".format(key, memory[key])
                              for key in sorted(memory.keys()))
            self.wfile.write(form.format(known).encode())

    def do_POST(self):
        # Decode the form data
        length = int(self.headers.get('Content-length', 0))
        body = self.rfile.read(length).decode()
        params = parse_qs(body)

        # Check the user submitted all form fields
        if "longuri" not in params or "shortname" not in params:
            # Serve 400 error with a useful message
            self.send_response(400)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Please fill both fields. :)".encode())
            return

        longuri = params["longuri"][0]
        shortname = params["shortname"][0]

        if CheckURI(longuri):
            # This URI is good! Remember it under the specified name
            memory[shortname] = longuri

            # Redirect to the root page (the form)
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            # Didn't successfully fetch the long URI
            # Send 404 error with a useful message
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Please make sure your Long URI '{}' exists. :)".format(longuri).encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, Shortener)
    httpd.serve_forever()
