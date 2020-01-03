from flask import Flask
from flask_restful import Resource, Api, reqparse
from resources.Result import Result

# EB looks for an 'application' callable by default.
application = Flask(__name__)
api = Api(application)

api.add_resource(Result, '/api/v1/results/<string:text>')

# run the app.
# Setting debug to True enables debug output. This line should be
# removed before deploying a production app.
if __name__ == '__main__':
    application.debug = True
    application.run()