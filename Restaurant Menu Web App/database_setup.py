import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# create instance of declarative base in order for class to inherit SQL features of SQLAlchemy
Base = declarative_base()

# table
class Restaurant(Base):
    __tablename__ = 'restaurant'
    # mapper, create columns with attributes
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(80))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    # define what data allowing API to access
    def serialize(self):
        # return object data in serializable format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


# create engine and connect to db
engine = create_engine('sqlite:///restaurantmenu.db')
# add classes as new tables in db within engine
Base.metadata.create_all(engine)
