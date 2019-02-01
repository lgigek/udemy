from flask import Flask
from flask_restful import Api

from math_operations import basic
from visit import visit

app = Flask(__name__)
api = Api(app)


api.add_resource(basic.Add, '/add')
api.add_resource(basic.Subtract, '/subtract')
api.add_resource(basic.Multiply, '/multiply')
api.add_resource(basic.Divide, '/divide')
api.add_resource(visit.Visit, '/visit')


@app.route('/')
def hello_world():
    return "Hello world"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
