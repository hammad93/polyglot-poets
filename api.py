import json
from flask import Flask, request
from flask_restplus import Resource, Api, fields, reqparse
from flask_cors import CORS, cross_origin

'''
polyglot-poets REST API
Hammad Usmani
Created: 4/14/19

This API will be run to generate a Swagger UI REST API for the polyglot-poets dataset.

Notes
-----
- Server automatically generates API documentation. To view the documentation, 
navigate to the specified directory for specifications according to OpenAPI. By
default this is the root director
'''
app = Flask(__name__)
api = Api(app, version='1.0', title='polyglot-poets API', description='OpenAPI')
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
app.config.SWAGGER_UI_JSONEDITOR = True
'''
API Model Declarations
----------------------
The following are the models for the appropriate api resources
'''