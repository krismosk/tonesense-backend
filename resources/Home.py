from flask_restful import Resource
from flask import jsonify

class Home(Resource):
  def get(self):
    message = {"test": "success"}
    response = jsonify(message)
    return response