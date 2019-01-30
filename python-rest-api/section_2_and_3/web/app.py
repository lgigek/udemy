from flask import Flask
from flask_restful import Api
import math_operations

app = Flask(__name__)
api = Api(app)


api.add_resource(math_operations.Add, '/add')
api.add_resource(math_operations.Subtract, '/subtract')
api.add_resource(math_operations.Multiply, '/multiply')
api.add_resource(math_operations.Divide, '/divide')


@app.route('/')
def hello_world():
    return "Hello world"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
