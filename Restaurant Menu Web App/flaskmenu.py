from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# jsonify can easily configure an API endpoint for app
# make an API endpoint (GET request)
@app.route('/restaurants/json/')
def restaurantJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[restaurant.serialize for restaurant in restaurants])


@app.route('/restaurant/<int:restaurant_id>/menu/json/')
def restaurantMenuJSON(restaurant_id):
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[item.serialize for item in items])


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/json/')
def restaurantMenuItemJSON(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=item.serialize)


# bind a function to an url
@app.route('/')
@app.route('/hello/')
@app.route('/restaurants/')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurant.html', restaurants=restaurants)


@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['restaurantname'])
        session.add(newRestaurant)
        session.commit()
        flash('New restaurant added!')
        return redirect(url_for('showRestaurants'))
    return render_template('newRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['updatedName']:
            editedRestaurant.name = request.form['updatedName']
        session.add(editedRestaurant)
        session.commit()
        flash('Restaurant updated!')
        return redirect(url_for('showRestaurants'))
    return render_template('editRestaurant.html', restaurant_id=restaurant_id, restaurant=editedRestaurant)


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    deletedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(deletedRestaurant)
        session.commit()
        flash('Restaurant deleted!')
        return redirect(url_for('showRestaurants'))
    return render_template('deleteRestaurant.html', restaurant_id=restaurant_id, restaurant=deletedRestaurant)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):
    # grab restaurant
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    # list menu item
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    '''
    output = ''
    for item in items:
        output += item.name
        output += '</br>'
        output += item.price
        output += '</br>'
        output += item.description
        output += '</br></br>'
    return output
    '''
    # html escaping: access python variables and functions, retrieve data from database and put in html
    # {% logical code %}, logical code to execute within html, e.g. for loop or statement
    # {{printed code}}, results to be printed in html
    # {% endfor %} or { % endif %}, indicate end of for loop or statement
    # render_template(template_name.html, variables needed to pass to template=keyword)
    return render_template('menu.html', restaurant=restaurant, items=items)


# URL building: create urls based on functions flask execute
# url_for('function', keyword arguments, ...)
@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form['description'], price=request.form['price'], course=request.form['course'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        # message flashing: prompt a message to user immediately after a certain action,
        # and disappear the next time the page is requested
        flash('New menu item created!')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    return render_template('newMenuItem.html', restaurant_id=restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['updatedName']:
            editedItem.name = request.form['updatedName']
        if request.form['updatedDescription']:
            editedItem.description = request.form['updatedDescription']
        if request.form['updatedPrice']:
            editedItem.price = request.form['updatedPrice']
        if request.form['updatedCourse']:
            editedItem.course = request.form['updatedCourse']
        session.add(editedItem)
        session.commit()
        flash('Menu item updated!')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    return render_template('editMenuItem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        flash('Menu item deleted!')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    return render_template('deleteMenuItem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=deleteItem)


if __name__ == '__main__':
    # session: enable server to store info across multiple webpages to create personalized user experience
    app.secret_key = 'super_secrete_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
