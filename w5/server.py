import datetime
from flask import Flask, jsonify, request
from names_ages import get_names_ages, add_name_age, edit_name_age, clear_names_ages

APP = Flask(__name__)

'''
CRUD: https://webcms3.cse.unsw.edu.au/static/uploads/course/COMP1531/21T3/f7a06cfde5506d83d6b1619c0c2af5eb722bc28aea4cbe00219bfd65abfbc3b2/COMP1531-4.2.pdf

data = request.get_json() vs request.args.get('min_age')
https://stackoverflow.com/questions/23326368/flask-request-args-vs-request-form
Decorator is a function which calls another function.
'''