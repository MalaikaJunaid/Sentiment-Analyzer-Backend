from functools import wraps
from flask import request

def log_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(f"Request to {request.path} with data: {request.json}")
        return f(*args, **kwargs)
    return decorated_function
