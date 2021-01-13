import app, requests, json
from functools import wraps
from app.exceptions.exceptions import *
import os 

def exceptions_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise
    return wrapper

class Controller():

    def __init__(self):
        self.var = "test"