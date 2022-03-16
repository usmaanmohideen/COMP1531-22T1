import datetime
from flask import Flask, jsonify, request
from names_ages import get_names_ages, add_name_age, edit_name_age, clear_names_ages

# fromtimestamp(): https://pythontic.com/datetime/date/fromtimestamp

APP = Flask(__name__)

@APP.route('/getnamesages', methods=['GET'])
def getnames():
    min_age = request.args.get('min_age')
    return jsonify(get_names_ages(min_age))

@APP.route('/addnameage', methods=['POST'])
def addname():
    data = request.get_json()
    name = data['name']
    dob = data['dob']

    add_name_age(name, dob)

    return {}

@APP.route('/editnameage', methods=['PUT'])
def editname():
    data = request.get_json()
    name = data['name']
    dob = data['dob']
    edit_name_age(name, dob)

    return {}

@APP.route('/clear', methods=['DELETE'])
def clear():
    clear_names_ages()
    return {}

if __name__ == '__main__':
    APP.run(debug=True, port=8080)