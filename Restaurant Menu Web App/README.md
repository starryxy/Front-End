# Restaurant Menu Web App

## Summary

A web application based on Flask that queries a database using an Object-Relational Mapping (ORM) layer for items on restaurant menus and then dynamically generates complete menus in the form of web pages and REST API endpoints. The web app also allows CRUD operations for restaurants and menu items.


## Files in Repo

- `README.md` <br>
brief intro of the project

- `database_setup.py` <br>
set up the database to store restaurants and menu items data

- `restaurantmenu.db` <br>
database that stores restaurants and menu items data

- `lotsofmenus.py` <br>
contain some fake restaurants and menu items data

- `flaskmenu.py` <br>
based on Flask, set up routing, convert GET and POST requests to CRUD operations with SQLAlchemy statements, add message flashing to give users feedback immediately after a certain action, configure REST API endpoints to return JSON objects when clients send GET requests

- /templates <br>
contain html templates that methods in `flaskmenu.py` can render

- /static <br>
css file that styles all web pages


## How to Run

1. Run database_setup.py to create the database <br>
`python database_setup.py`

2. Run lotsofmenus.py to populate the database <br>
`python lotsofmenus.py`

3. Run flaskmenu.py and navigate to http://0.0.0.0:5000/ in your browser <br>
`python flaskmenu.py`


## Web App Functionalities

http://0.0.0.0:5000/, http://0.0.0.0:5000/hello, or http://0.0.0.0:5000/restaurants/ show all the restaurants
![](static/restaurants.png)

Add new restaurant
![](static/add_new_restaurant.png)

Edit existing restaurant name
![](static/edit_restaurant.png)

Delete existing restaurant
![](static/delete_restaurant.png)

http://0.0.0.0:5000/restaurant/%restaurant_id%, and http://0.0.0.0:5000/restaurant/%restaurant_id%/menu show all the menu items that restaurant has
![](static/menu.png)

If the restaurant doesn't have any menu item yet, show as below
![](static/no_item_menu.png)

Add new menu item
![](static/add_menu_item.png)

Edit existing menu item name, description, price, course
![](static/edit_menu_item.png)

Delete existing menu item name
![](static/delete_menu_item.png)

http://0.0.0.0:5000/restaurants/json, return JSON object for all restaurants
![](static/restaurants_json.png)

http://0.0.0.0:5000/restaurant/%restaurant_id%/menu/json, return JSON object for all menu items of the restaurant
![](static/restaurant_menu_items_json.png)

http://0.0.0.0:5000/restaurant/%restaurant_id%/menu/%menu_id%/json, return JSON object for the menu item
![](static/menu_item_json.png)
