# ToneSense

## Introduction
ToneSense is a web app that allows a user to enter in a sentence and receive a sentiment analysis result from a Machine Learning Model. This repository contains the source code for the RESTful API built in Flask.

This project was built in two separate and distinct parts: Version 1 relies on a external API with a pre-trained model and Version 2 uses a self fine tuned model. Explained in more detail below.

## Version 1
This version utilizes the Google Cloud NLP API to analyze the user's sentence and return a sentiment analysis result.  

The API will return a numbered score and magnitude which represents the sentence's sentiment on a scale of -1.0 to 1.0. The scoring range is as follows: 0.25 to 1.0 corresponds to a result of "likely positive", -0.25 to 0.25 corresponds to a result of "likely neutral", and -1.0 to -0.25 returns corresponds to a of "likely negative".

### Installation
1. Make a clone of this repository. 
2. Checkout the master branch.
3. Install Anaconda.
4. Activate a new Conda environment.
5. Install Python 3.7.4.
6. Install dependencies using pip `pip install -r requirements.txt` or using Conda `conda install --file requirements.txt`
7. Create a Google Cloud Platform account.
8. Follow installation instructions to get started with [Cloud Natural Language API](https://cloud.google.com/natural-language/docs/quickstarts).
9. Install and initialize [Cloud SDK.](https://cloud.google.com/sdk/docs/)
10. Run server locally `python application.py`
11. To interact with model and see its results in the Web App, follow the installation instructions in the corresponding repository. [Linked here.](https://github.com/krismosk/frontend-capstone-2)

Deployed with AWS Elastic Beanstalk. [View here.](http://backend-capstone2-dev.us-west-2.elasticbeanstalk.com/)

## Version 2
This version was built using a Naive Bayes Classifier model and fine tuned with the Natural Language Toolkit (NLTK). The model was fine tuned in a Google Colab notebook. [Linked here.](https://colab.research.google.com/drive/1QttwHHLlbxLzFAl1jPFqZjAZ7xEnO-K6)

The ML model implements binary classification, therefore the results returned are either "positive" or "negative", with the score 1.0 or -1.0, respectively.

### Installation
1. Make a clone of this repository.
2. Checkout the ml_version branch.
3. Install Anaconda.
4. Activate a new Conda environment.
5. Install Python 3.7.4.
6. Install dependencies using pip `pip install -r requirements.txt` or using Conda `conda install --file requirements.txt`
7. Run server locally `python application.py`
8. To interact with model and see its results in the Web App, follow the installation instructions in the corresponding repository. [Linked here.](https://github.com/krismosk/frontend-capstone-2)

Deployed with [INSERT NAME HERE]. View here.

## API 
- Route: '/api/v1/results/{string:text}'
- Parameter: String, spaces allowed