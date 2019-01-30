from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/add_two_numbers', methods=['POST'])
def add_two_numbers():
    data_dictionary = request.get_json()
    x = data_dictionary['x']
    y = data_dictionary['y']

    result = x + y

    return_json = {
        'result': result
    }

    return jsonify(return_json), 200


if __name__ == '__main__':
    app.run(debug=True)
