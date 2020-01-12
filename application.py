from flask import Flask
from flask_restful import Resource, Api, reqparse
from resources.Result import Result
from resources.Home import Home
import os
from dotenv import load_dotenv
import logging

# import the google cloud client library
# from google.cloud import language
# from google.cloud.language import enums
# from google.cloud.language import types

# logging.basicConfig(filename='/tmp/tmp.log',level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

# load dotenv in the base root
# APP_ROOT = os.path.join(os.path.dirname(__file__), '..') 
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)
load_dotenv(verbose=True)
logging.info(os.environ)
logging.info(os.getcwd())

logging.warning(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))

application = api = Flask(__name__)

api = Api(application)

api.add_resource(Result, '/api/v1/results/<string:text>')
api.add_resource(Home, '/')

if __name__ == '__main__':
    application.run(debug=False)