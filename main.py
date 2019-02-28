from typing import Dict, Callable, Any
from flask import Flask, jsonify, request, abort

from apis import blueprint
from classes.MyApi import (
    myApiNamespace,
    myApiPaths,
    MyApiRequestDev,
    MyApiRequestProd,
)

EncryptAPICallable = Callable[[Any], Dict[str, str]]

app = Flask(__name__)
app.register_blueprint(blueprint)
app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

# we can only deploy one function to firebase, this will map all routes to one endpoint
def buildFirebasePath(path: str) -> str:
    return '/' + myApiNamespace + path

methods: Dict[str, EncryptAPICallable] = {
    buildFirebasePath(myApiPaths['dev']): MyApiRequestDev.post,
    buildFirebasePath(myApiPaths['prod']): MyApiRequestProd.post,
}

def dispatchRequest(request: Any = request):
    if (request.path in methods):
        return methods[request.path](request)

    return abort(404)

# this one will be deployed to firebase
firebaseRequest = dispatchRequest
