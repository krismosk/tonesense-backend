from flask import Flask
from flask_restful import Resource, Api
from resources.Result import Result

app = Flask(__name__)
api = Api(app)

api.add_resource(Result, '/api/v1/results')

if __name__ == '__main__':
    app.run(debug=True)