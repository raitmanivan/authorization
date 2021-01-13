from flask import Flask, request, jsonify
from app.blueprint import blueprint
from app.modules import controller
from app.resources.middleware import Middleware
import os

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.register_blueprint(blueprint, url_prefix="/")
    return app

@blueprint.before_request
def before_all_requests():
    scope = "Test"
    middleware = Middleware()
    if not middleware.request_interceptor(request.headers,scope):
        return jsonify({'Desc': 'Unauthorized'}),401