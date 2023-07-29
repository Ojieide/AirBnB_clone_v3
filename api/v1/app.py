#!/usr/bin/python3
""" Returns the status of API """
import os
from flask import Flask, jsonify
from flask_cors import CORS

from models import storage
from api.v1.views import app_views


app = Flask(__name__)
""" Creates a variable app, instance of Flask """
app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(os.getenv('HBNB_API_PORT', '5000'))
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': app_host}})


@app.teardown_appcontext
def teardown_flask(exception):
    """ Method to handle @app.teardown_appcontext """
    # print(exception)
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """
    Creates a handler for 404 errors that returns a
    JSON-formatted 404 status code response
    """
    return jsonify(error='Not found'), 404


@app.errorhandler(400)
def error_400(error):
    """
    Creates a handler for 400 errors that returns a
    JSON-formatted 400 status code response
    """
    msg = 'Bad request'
    if isinstance(error, Exception) and hasattr(error, 'description'):
        msg = error.description
    return jsonify(error=msg), 400


if __name__ == '__main__':
    app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    app_port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(
        host=app_host,
        port=app_port,
        threaded=True
    )
