from flask_restful import Resource

results = [
  {
    "sentence_0": {
      "score": -0.6,
      "magnitude": 3.3,
    }
  },
  {
    "sentence_1": {
      "score": 0,
      "magnitude": 4.7,
    }
  },
  {
    "sentence_2": {
      "score": -0.1,
      "magnitude": 1.8,
    }
  },
]

class Result(Resource):
  def get(self):
    return results