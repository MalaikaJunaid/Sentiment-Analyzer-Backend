from functools import wraps
from flask import request, jsonify

def basic_authentication(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token == 'Bearer secret-token':  # Replace 'secret-token' with a real token in production
            return f(*args, **kwargs)
        else:
            return jsonify({'message': 'Unauthorized'}), 401
    return decorated_function
