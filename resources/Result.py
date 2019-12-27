from flask_restful import Resource

# import the google cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
  
# instantiates a client
client = language.LanguageServiceClient()

# the text to analyze
text = u'I love you, Hilter!'
document = types.Document(
  content=text,
  language='en',
  type=enums.Document.Type.PLAIN_TEXT)

# detect the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment
response = client.analyze_entity_sentiment(document=document, encoding_type='UTF32')

entities = response.entities

# print results
print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
print('Entity Sentiment: {}, {}'.format(entities[0].sentiment.score, entities[0].sentiment.magnitude))

results = [
  {
    "sentence": {
      "score": -0.6,
      "magnitude": 3.3,
    }
  },
  {
    "sentence": {
      "score": 0,
      "magnitude": 4.7,
    }
  },
  {
    "sentence": {
      "score": -0.1,
      "magnitude": 1.8,
    }
  },
]

class Result(Resource):
  def get(self):
    return results