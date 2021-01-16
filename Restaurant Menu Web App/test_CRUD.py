# CRUD
# Create = Insert into
# Read = Select
# Update = Update
# Delete = Delete

# ORM: Object-relational mapping, is a programming technique for converting data
# between incompatible type systems using object-oriented programming languages.

python database_setup.py

python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
# bind engine with base to make connections between class definitions and tables in db
Base.metadata.bind = engine
# establish link of communication between code executions and engine
# SQLAlchemy executes CRUD operations via session
DBSession = sessionmaker(bind = engine)
# initiate a session object
session = DBSession()

# CREATE
# create new data entry in Restaurant table
myFirstRestaurant = Restaurant(name = "Pizza Palace")
# staging data entry in session
session.add(myFirstRestaurant)
# commit data entry from session to db
session.commit()
# find Restaurant table in db, find all entries in the table and return in a list
session.query(Restaurant).all()
# find an object at this location in memory
# [<database_setup.Restaurant object at 0x1051744a8>]
# create new data entry in MenuItem table
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()

# READ
# extract single row
firstResult = session.query(Restaurant).first()
firstResult.name

python lotsofmenus.py

session.query(Restaurant).all()
# for loop to display each row in name column
items = session.query(MenuItem).all()
for item in items:
    print(item.name)
# https://docs.sqlalchemy.org/en/13/orm/session_basics.html#basics-of-using-a-session

# UPDATE
# https://docs.sqlalchemy.org/en/13/orm/query.html
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print("\n")

# return only one object instead of a list
urbanVeggieBurger = session.query(MenuItem).filter_by(id = 10).one()
print(urbanVeggieBurger.price)
# change price of Veggie Burger in Urban Burger restaurant from $5.99 to $2.99
urbanVeggieBurger.price = "$2.99"
session.add(urbanVeggieBurger)
session.commit()
# change price of Veggie Burger in all restaurants to $2.99
for veggieBurger in veggieBurgers:
    if veggieBurger.price != "$2.99":
        veggieBurger.price = "$2.99"
        session.add(veggieBurger)
        session.commit()
# check prices are changed
for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print("\n")

# DELETE
spinach = session.query(MenuItem).filter_by(name = "Spinach Ice Cream").one()
print(spinach.restaurant.name)
session.delete(spinach)
session.commit()
# search gives no row was found result
session.query(MenuItem).filter_by(name = "Spinach Ice Cream").one()
