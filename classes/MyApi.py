from typing import Dict
from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields
from flask_cors import cross_origin
import json

myApiNamespace = 'myApi'
ns = Namespace(myApiNamespace, description='myApi operations')

myApiPaths = {
    'dev': '/message-dev',
    'prod': '/message',
}

myApiResponse = ns.model('myApiResponse', {
    'id': fields.String(description='reference id', example='E0', required=True),
    'message': fields.String(description='message', required=True),
})

@ns.route(myApiPaths['dev'])
class MyApiRequestDev(Resource):
    @staticmethod
    @cross_origin()
    @ns.doc(params={'payload': {'in': 'body', 'type': 'object'}})
    @ns.response(200, 'OK', myApiResponse)
    @ns.response(400, 'payload body not valid')
    def post(request = request) -> Dict[str, str]:
        """My API endpoint for development"""

        return jsonify({'id': 'E0', 'message': 'from dev'})

@ns.route(myApiPaths['prod'])
class MyApiRequestProd(Resource):
    @staticmethod
    @cross_origin(origins = '^https://request.thaicashdd.com$')
    @ns.doc(params={'payload': {'in': 'body', 'type': 'object'}})
    @ns.response(200, 'OK', myApiResponse)
    @ns.response(400, 'payload body not valid')
    def post(request = request) -> Dict[str, str]:
        """My API endpoint for production"""

        return jsonify({'id': 'E0', 'message': 'from prod'})
