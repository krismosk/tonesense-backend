from flask_restful import Resource, reqparse
from flask import jsonify
import json
import logging

# import the google cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

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
    result['score'] = -1.0
    result['magnitude'] = 0.9
    response = jsonify(result)
    return response

  def get_sentiment(self, text):
    result = {}
    try:
      logging.info("get sentiment")
      # instantiates a client
      client = language.LanguageServiceClient()
      # the text to analyze
      analyzed_text = text
      document = types.Document(
        content=analyzed_text,
        language='en',
        type=enums.Document.Type.PLAIN_TEXT)
      logging.info("document created: {}".format(document))

      # detect the sentiment of the text
      sentiment = client.analyze_sentiment(document=document).document_sentiment
      logging.info("analyzed sentiment")

      entity_response = client.analyze_entity_sentiment(document=document, encoding_type='UTF32')
      logging.info("sentiment done")

      result['text'] = text
      result['score'] = sentiment.score
      result['magnitude'] = sentiment.magnitude
      result['entities'] = []

      for entity in entity_response.entities:
        result['entities'].append({'name': entity.name, 'type': entity.type, 'salience': entity.salience})
    except:
      logging.warn("exception")
      e = sys.exc_info()[0]
      logging.error(e)
    finally:
      print('result printed:')
      print(result)
      return jsonify(result)
    



