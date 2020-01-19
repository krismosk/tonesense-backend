from flask_restful import Resource, reqparse
from flask import jsonify
import json
import logging
import pickle
import re, string
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier

nltk.data.path.append('./nltk_data/')

def remove_noise(tweet_tokens, stop_words = ()):
  cleaned_tokens = []

  for token, tag in pos_tag(tweet_tokens):
      token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                      '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
      token = re.sub("(@[A-Za-z0-9_]+)","", token)

      if tag.startswith("NN"):
          pos = 'n'
      elif tag.startswith('VB'):
          pos = 'v'
      else:
          pos = 'a'

      lemmatizer = WordNetLemmatizer()
      token = lemmatizer.lemmatize(token, pos)

      if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
          cleaned_tokens.append(token.lower())
  return cleaned_tokens

class NaiveBayes(Resource):
  def post(self, text):
    text = text
    testing = False
    if testing:
      return self.get_mock_sentiment(text)
    else:
      return self.get_ml_sentiment(text)
    
  def get_mock_sentiment(self, text):
    result = {}
    result['text'] = text
    result['score'] = -1.0
    result['magnitude'] = 0.9
    response = jsonify(result)
    return response

  def get_ml_sentiment(self, text):
    custom_tokens = remove_noise(word_tokenize(text))
    with open('classifier.pickle', 'rb') as f:
      classifier = pickle.load(f)

    result = classifier.classify(dict([token, True] for token in custom_tokens))
    if result == "Positive":
      response = {
        "text": f"{text}",
        "score": "1.0"
      }
    elif result == "Negative":
      response = {
        "text": f"{text}",
        "score": "-1.0"
        }
    return jsonify(response)