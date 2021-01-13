import app, json
from app.exceptions.exceptions import *
from flask import Blueprint, jsonify, request
from functools import wraps
import traceback

blueprint = Blueprint("blueprint", __name__)

def exceptions_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidCredentials:
            return jsonify({'Desc': 'Unauthorized'}),403
        except Exception as e:
            return jsonify({'Desc': "There was an error"}), 500
    return wrapper

@blueprint.route("/ping")
def main():
    return "pong"