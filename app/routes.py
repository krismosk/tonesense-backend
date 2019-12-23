from app import app
from flask import request, jsonify

# create some test data
results = [
  {'id': 0, 
  'tone': 'positive'
  },
  {'id': 1, 
  'tone': 'negative'
  },
  {'id': 2, 
  'tone': 'neutral'
  },
]

@app.route('/')
@app.route('/index', methods=['GET'])
@app.route('/results', methods=['GET'])
def index():
    return "Hello, World!"

# route to return all of the results in json
def results():
  return jsonify(results)


app.run()