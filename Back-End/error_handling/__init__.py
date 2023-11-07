from flask import jsonify
from werkzeug.exceptions import HTTPException
from .custom_errors import CategoricalHandlingError


def handle_error(error):
    m = error.args[0]
    response = {
        'status': 'error',
        'message': m
    }
    return jsonify(response)