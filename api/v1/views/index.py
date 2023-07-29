#!/usr/bin/python3
""" Imports app_views from api.v1.views """
from flask import jsonify

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def get_status():
    """
    Creates a route /status on the object app_views
    that returns a JSON string
    """
    return jsonify(status='OK')


@app_views.route('/stats')
def get_stats():
    """Creates an endpoint that retrieves the number
    of each objects by type
    """
    objects = {
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review,
        'states': State,
        'users': User
    }
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)
