from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

# import CRUD operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<a href='/restaurants/new'>Create a New Restaurant Here</a><br><br>"
                for restaurant in restaurants:
                    output += restaurant.name
                    # direct to edit/delete link with restaurant id
                    output += "<br><a href='/restaurants/{}/edit'>Edit</a>".format(restaurant.id)
                    output += "<br><a href='/restaurants/{}/delete'>Delete</a>".format(restaurant.id)
                    output += "<br><br><br>"
                output += "</body></html>"
                self.wfile.write(output.encode())
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                # show a form to add new restaurant
                form = '''<!DOCTYPE html>
                <h1>Create a New Restaurant</h1>
                <form method="POST">
                    <input type="text" name="newRestaurantName" placeholder="New Restaurant Name">
                    <button type="submit">Create</button>
                </form>
                '''
                self.wfile.write(form.encode())
                return

            if self.path.endswith("/edit"):
                restaurantID = self.path.split("/")[2]
                findRestaurant = session.query(Restaurant).filter_by(id=restaurantID).one()
                if findRestaurant:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    # rename existing restaurant
                    output = ""
                    output += "<html><body>"
                    output += "<h1>{}</h1>".format(findRestaurant.name)
                    output += "<form method = 'POST'>"
                    output += "<input type = 'text' name = 'updatedName' placeholder = '{}' >".format(findRestaurant.name)
                    output += "<button type = 'submit'>Rename</button>"
                    output += "</form></body></html>"
                    self.wfile.write(output.encode())

            if self.path.endswith("/delete"):
                restaurantID = self.path.split("/")[2]
                findRestaurant = session.query(Restaurant).filter_by(id=restaurantID).one()
                if findRestaurant:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    # delete existing restaurant
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete <span style='color: red'>{}</span> restaurant?</h1>".format(findRestaurant.name)
                    output += "<br><form method = 'POST'>"
                    output += "<button type = 'submit'>Delete</button>"
                    output += "<br><br><a href='/restaurants'>Cancel</a>"
                    output += "</form></body></html>"
                    self.wfile.write(output.encode())

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                # Decode the form data
                length = int(self.headers.get('Content-length', 0))
                data = self.rfile.read(length).decode()
                restaurantname = parse_qs(data)["newRestaurantName"][0]

                # Create new Restaurant Object
                NewRestaurant = Restaurant(name=restaurantname)
                session.add(NewRestaurant)
                session.commit()

                self.send_response(303)  # redirect via GET
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

            if self.path.endswith("/edit"):
                length = int(self.headers.get('Content-length', 0))
                data = self.rfile.read(length).decode()
                updatedRestaurantName = parse_qs(data)["updatedName"][0]

                restaurantID = self.path.split("/")[2]
                findRestaurant = session.query(Restaurant).filter_by(id=restaurantID).one()
                if findRestaurant:
                    findRestaurant.name = updatedRestaurantName
                    session.add(findRestaurant)
                    session.commit()

                    self.send_response(303)  # redirect via GET
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/delete"):
                restaurantID = self.path.split("/")[2]
                findRestaurant = session.query(Restaurant).filter_by(id=restaurantID).one()
                if findRestaurant:
                    session.delete(findRestaurant)
                    session.commit()

                    self.send_response(303)  # redirect via GET
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except IOError:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()


if __name__ == '__main__':
    main()

