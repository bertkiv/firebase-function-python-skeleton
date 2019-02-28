from flask import Blueprint
from flask_restplus import Api

from classes.MyApi import ns as ns1

blueprint = Blueprint('api', __name__)
api = Api(blueprint, appversion='1.0', title='My API', description='My API endpoint')

api.add_namespace(ns1)
