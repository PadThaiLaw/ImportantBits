#!/usr/bin/env python

import requests
import json
import os

# 1 get citation information from canlii for cited case
# 2 for each citing case
#   a get text of citing case from canlii
#   b locate citations to cited case
#   c determine paragraph reference
#   d determine sentiment
#   e put into DB

# CanLII constants
CASEID = "2007fca198"
CANLII_CASE_DATABASE="csc-scc/"
CANLII_BASE_URL = "http://api.canlii.org/v1/"
CANLII_CITATOR = "caseCitator/"
CANLII_LANGUAGE= "en/"

# global variables - BAD
citing_cases = []

class CanLIIConnection:

  def citing_cases(self):
    url = CANLII_BASE_URL + CANLII_CITATOR + CANLII_LANGUAGE
    url += CANLII_CASE_DATABASE + CASEID + "/citingCases"
    url += "?api_key=" + CANLII_API_KEY

    r = requests.get(url)
    body = json.loads(r.text)
    array = body['citingCases']

    for item in array:
      citing_cases.append(item['caseId']['en'])
      # print(item['caseId']['en'])

# get environment variables
CANLII_API_KEY = os.environ['CANLII_KEY']

# run CanLII query
cc = CanLIIConnection()
cc.citing_cases()

# run next query


# Class to track what to post onto the database
class APIModel:
  # Initialize by calling APIModel(canliiIDString, paragraph number, citation count and sentiment int), APIModel("2002bcca12, 33, 0, 0")
  def __init__(self, canlii_id_str, paragraph_num_int, citation_count_int, sentiment_sum_int):
    self.canlii_id = canlii_id_str
    self.paragraph_num = paragraph_num_int
    self.citation_count = citation_count_int
    self.sentiment_sum = sentiment_sum_int
  # Function to post to database
  def post(self):
    content = {
      "canlii_id": self.canlii_id,
      "citation_count": self.citation_count,
      "paragraph_num": self.paragraph_num,
      "sentiment_sum": self.sentiment_sum
      }
    request = requests.post("http://importantbits.pythonanywhere.com/api/citation/", json=content)
  # Function to increment by 1
  def increment_count(self):
    self.citation_count += 1
  # Function to set sentiment
  def set_sentiment(self, new_sentiment):
    self.sentiment = new_sentiment
  # Print in reader friendly format
  def print(self):
    printstring = self.canlii_id + " at paragraph " + str(self.paragraph_num) + ", cited " +str(self.citation_count) + " times and has sentiment score of " + str(self.sentiment_sum)
    print(printstring)