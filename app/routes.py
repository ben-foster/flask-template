from flask import Blueprint, jsonify
from flask_cors import CORS

routes = Blueprint('routes', __name__)
CORS(routes)

@routes.before_request
def before_request():
    pass

@routes.route('/')
def main():
    return jsonify({'message': 'Hello World!'})