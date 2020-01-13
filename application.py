from flask import Flask
from flask_restful import Resource, Api, reqparse
from resources.Result import Result
from resources.Home import Home
from resources.NaiveBayes import NaiveBayes
import os
from dotenv import load_dotenv
import logging

load_dotenv(verbose=True)
logging.info(os.environ)
logging.info(os.getcwd())

logging.warning(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))

application = api = Flask(__name__)

api = Api(application)

api.add_resource(Result, '/api/v1/results/<string:text>')
api.add_resource(NaiveBayes, '/api/v2/results/<string:text>')
api.add_resource(Home, '/')

if __name__ == '__main__':
    application.run(debug=False)