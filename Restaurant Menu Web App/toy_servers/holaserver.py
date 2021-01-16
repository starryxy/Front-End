# https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_response
from http.server import BaseHTTPRequestHandler, HTTPServer

class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>Hello!</body></html>"
            self.wfile.write(message.encode())
            # print(message)
            return
        elif self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body> &#161 Hola ! <a href = '/hello'> Back to Hello </a></body></html>"
            self.wfile.write(message.encode())
            # print(message)
            return
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)


# instantiate server and specify the port it will listen on
def main():
    try:
        port = 8080
        # server address is a tuple containing host and port
        server = HTTPServer(('', port), WebServerHandler)
        print("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()
