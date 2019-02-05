from flask_restful import Resource, request
from src.user import User


class Sentence(Resource):
    @staticmethod
    def post():
        request_json = request.get_json()
        if not Sentence._is_parameters_correct_for_post(request_json):
            return {'Message': 'Incorrect parameters'}, 400

        username = request_json['username']
        if not User.is_user_registered(username):
            return {'Message': 'Username not found'}, 404

        if not User.is_password_correct(username, request_json['password']):
            return {'Message': 'Incorrect user/password'}, 400

        number_of_tokens = User.get_number_of_tokens(username)
        if number_of_tokens <= 0:
            return {'Message': 'Out of tokens'}, 400

        User.update_sentence_and_remove_a_token(username, request_json['sentence'], number_of_tokens)
        return {'Message': 'Sentence updated'}, 200

    @staticmethod
    def get():
        request_json = request.get_json()
        if not Sentence._is_parameters_correct_for_get(request_json):
            return {'Message': 'Incorrect parameters'}, 400

        username = request_json['username']
        if not User.is_user_registered(username):
            return {'Message': 'Username not found'}, 404

        if not User.is_password_correct(username, request_json['password']):
            return {'Message': 'Incorrect user/password'}, 400

        return {'Sentence': User.get_sentence(username)}, 200

    @staticmethod
    def _is_parameters_correct_for_post(request_json):
        if 'username' not in request_json or 'password' not in request_json or 'sentence' not in request_json:
            return False
        else:
            return True

    @staticmethod
    def _is_parameters_correct_for_get(request_json):
        if 'username' not in request_json or 'password' not in request_json:
            return False
        else:
            return True
