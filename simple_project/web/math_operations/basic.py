from flask import request
from flask_restful import Resource


class Add(Resource):
    # This method is executed if resource add (/add) was called with method POST
    @staticmethod
    def post():
        posted_data = request.get_json()

        status_code = _get_status_code_according_to_parameters(posted_data, 'add')
        if status_code != 200:
            return {'Message': 'There was an error'}, status_code

        x = int(posted_data['x'])
        y = int(posted_data['y'])

        return {'Message': x + y}, status_code


class Subtract(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()

        status_code = _get_status_code_according_to_parameters(posted_data, 'subtract')
        if status_code != 200:
            return {'Message': 'There was an error'}, status_code

        x = int(posted_data['x'])
        y = int(posted_data['y'])

        return {'Message': x - y}, status_code


class Multiply(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()

        status_code = _get_status_code_according_to_parameters(posted_data, 'multiply')
        if status_code != 200:
            return {'Message': 'There was an error'}, status_code

        x = int(posted_data['x'])
        y = int(posted_data['y'])

        return {'Message': x * y}, status_code


class Divide(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()

        status_code = _get_status_code_according_to_parameters(posted_data, 'divide')
        if status_code != 200:
            return {'Message': 'There was an error'}, status_code

        x = int(posted_data['x'])
        y = int(posted_data['y'])

        return {'Message': x / y}, status_code


def _get_status_code_according_to_parameters(posted_data, function_name):
    if not _verify_if_parameters_exist(posted_data):
        return 400  # Missing parameters
    elif not _verify_if_parameters_are_int(posted_data):
        return 400
    elif function_name == 'divide' and int(posted_data['y']) == 0:
        return 400  # Can not divide by 0
    else:
        return 200


def _verify_if_parameters_exist(posted_data):
    if 'x' not in posted_data or 'y' not in posted_data:
        return False
    else:
        return True


def _verify_if_parameters_are_int(posted_data):
    try:
        int(posted_data['x'])
        int(posted_data['y'])
        return True
    except ValueError:
        return False
