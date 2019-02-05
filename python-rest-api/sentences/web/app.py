from flask import Flask
from flask_restful import Api
from src.user import User
from src.sentence import Sentence

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user')
api.add_resource(Sentence, '/sentence')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
