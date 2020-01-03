from flask import Flask
from flask_restful import Resource, Api, reqparse
from resources.Result import Result
from resources.Home import Home

app = Flask(__name__)
api = Api(app)

api.add_resource(Result, '/api/v1/results/<string:text>')
api.add_resource(Home, '/api/v1')

if __name__ == '__main__':
    app.run(debug=True)