# ToneSense

## Introduction
ToneSense is a React web app that allows a user to enter in a sentence and receive a sentiment analysis result from a Machine Learning Model. This repository contains the source code for the RESTful API built in Flask.

This project was built in two separate parts: Version 1 relies on a external API with a pre-trained model and Version 2 uses a self fine tuned model. Explained in more detail below.

Deployed with [Google App Engine.](https://tonesense.appspot.com)

## Version 1
This version utilizes the Google Cloud NLP API to analyze the user's sentence and return a sentiment analysis result.  

The API will return a numbered score and magnitude which represents the sentence's sentiment on a scale of -1.0 to 1.0. The scoring range is as follows: 0.25 to 1.0 corresponds to a result of "likely positive", -0.25 to 0.25 corresponds to a result of "likely neutral", and -1.0 to -0.25 returns corresponds to a result of "likely negative".

## Version 2
This version was built using a Naive Bayes Classifier model and fine tuned with the Natural Language Toolkit (NLTK). The model was fine tuned in [Google Colab.](https://colab.research.google.com/drive/1QttwHHLlbxLzFAl1jPFqZjAZ7xEnO-K6)

The ML model implements binary classification, therefore the results returned are either "positive" or "negative", with the score 1.0 or -1.0, respectively.

### Installation
1. Make a clone of this repository. 
2. Checkout the master branch.
3. Install [Anaconda.](https://www.anaconda.com/distribution/)
4. Activate a new Conda environment.
5. Install Python 3.7.4.
6. Install dependencies using pip `pip install -r requirements.txt` or using Conda `conda install --file requirements.txt`
7. Create a [Google Cloud Platform account.](https://cloud.google.com/gcp/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-skws-all-all-trial-p-dr-1008076&utm_content=text-ad-none-any-DEV_c-CRE_109860918967-ADGP_Hybrid+%7C+AW+SEM+%7C+SKWS+%7C+US+%7C+en+%7C+Multi+~+Cloud-KWID_43700010806032907-kwd-171201442&utm_term=KW_cloud-ST_cloud&gclid=Cj0KCQiAvJXxBRCeARIsAMSkApphkSbzVpyD5yAO5JW2kGvCo5vgE2SJTMcJAZbZR-JzcC_St8Kwc0kaAkzfEALw_wcB)
8. Follow installation instructions to get started with [Cloud Natural Language API.](https://cloud.google.com/natural-language/docs/quickstarts)
9. Install and initialize [Cloud SDK.](https://cloud.google.com/sdk/docs/)
10. Run server locally `python application.py`
11. To interact with model and see its results in the Web App, follow the installation instructions in the [corresponding repository.](https://github.com/krismosk/frontend-capstone-2)

## API 
- Google NLP Route: '/api/v1/results/{string:text}'
  - Parameter: String, spaces allowed
- Naive Bayes Classifier Route: '/api/v2/results/{string:text}'
  - Parameter: String, spaces allowed
  
## Demo
[![ToneSense Demo](http://img.youtube.com/vi/cTv0F3Z7DK4/0.jpg)](http://www.youtube.com/watch?v=cTv0F3Z7DK4 "ToneSense Demo")

ToneSense is developed by Kristina Moskalets as a capstone project for [Ada Developers Academy](https://adadevelopersacademy.org/).
