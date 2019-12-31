from flask_restful import Resource, reqparse
from flask import jsonify
import json

# import the google cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.protobuf.json_format import MessageToDict

class Result(Resource):
  def post(self, text):
    text = text
    testing = False
    if testing:
      return self.get_mock_sentiment(text)
    else:
      return self.get_sentiment(text)
    
  def get_mock_sentiment(self, text):
    result = {}
    result['text'] = text
    result['score'] = 0.8
    result['magnitude'] = 0.9
    response = jsonify(result)
    return response

  def get_sentiment(self, text):
    # instantiates a client
    client = language.LanguageServiceClient()
    
    # the text to analyze
    analyzed_text = text
    document = types.Document(
      content=analyzed_text,
      language='en',
      type=enums.Document.Type.PLAIN_TEXT)

    # detect the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    entity_response = client.analyze_entity_sentiment(document=document, encoding_type='UTF32')

    print('moskalets')
    result = {}
    result['text'] = text
    result['score'] = sentiment.score
    result['magnitude'] = sentiment.magnitude
    result['entities'] = []

    for entity in entity_response.entities:
      result['entities'].append({'name': entity.name, 'type': entity.type, 'salience': entity.salience})

    print('result printed:')
    print(result)

    response = jsonify(result)
    return response