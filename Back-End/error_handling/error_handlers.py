from flask import jsonify
from werkzeug.exceptions import HTTPException

# General Error Handler Definition
def handle_error(error):
    m = error.args[0]
    response = {
        'status': 'error',
        'message': m
    }
    return jsonify(response)

def handle_InvalidSeqError(error):
    response = {
        'status': 'error',
        'message': error.message,
        'tip': error.tip
    }
    return jsonify(response), 400