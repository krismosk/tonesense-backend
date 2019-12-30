from flask_restful import Resource, reqparse
from flask import jsonify

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
    response = client.analyze_entity_sentiment(document=document, encoding_type='UTF32')

    entities = response.entities

    # print('Text: {}'.format(text))
    # print('Entity Sentiment: {}, {}'.format(entities[0].sentiment.score, entities[0].sentiment.magnitude))
    print('moskalets')
    print(type(text))
    result = {}
    result['text'] = text
    result['score'] = sentiment.score
    result['magnitude'] = sentiment.magnitude
    # comment out this line to avoid TypeError: Object of type RepeatedCompositeContainer is not JSON serializable
    # result['entities'] = entities 
    print('result printed:')
    print(result)

    response = jsonify(result)
    print('response printed:')
    print(response)
    return response