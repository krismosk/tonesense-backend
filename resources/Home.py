from flask_restful import Resource
from flask import jsonify

class Home(Resource):
  def get(self):
    message = {"message": "success"}
    response = jsonify(message)
    return response