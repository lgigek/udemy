from flask_restful import Resource, request
from dbs.mongo import users
import bcrypt


class User(Resource):
    @staticmethod
    def post():
        request_json = request.get_json()
        if not User._is_parameters_present(request_json):
            return {'Message': 'Incorrect parameters'}, 400

        username = request_json['username']
        if User.is_user_registered(username):
            return {'Message': f'The user {username} is already registered'}, 400

        hashed_pw = bcrypt.hashpw(request_json['password'].encode('utf8'), bcrypt.gensalt())

        users.insert({
            'username': username,
            'password': hashed_pw,
            'sentence': '',
            'token': 5
        })

        return {'Message': 'Successfully signed up for API'}, 200

    @staticmethod
    def is_password_correct(username, password):
        hashed_password = users.find({'username': username})[0]['password']
        if bcrypt.hashpw(password.encode('utf8'), hashed_password) == hashed_password:
            return True
        else:
            return False

    @staticmethod
    def get_number_of_tokens(username):
        return users.find({'username': username})[0]['token']

    @staticmethod
    def update_sentence_and_remove_a_token(username, sentence, number_of_tokens):
        users.update({'username': username}, {
            '$set': {
                'sentence': sentence,
                'token': number_of_tokens - 1
            }
        })

    @staticmethod
    def get_sentence(username):
        return users.find({'username': username})[0]['sentence']

    @staticmethod
    def is_user_registered(username):
        if users.find({'username': username}).count() > 0:
            return True
        else:
            return False

    @staticmethod
    def _is_parameters_present(request_json):
        if 'username' not in request_json or 'password' not in request_json:
            return False
        else:
            return True
