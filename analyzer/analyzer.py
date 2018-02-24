#!/usr/bin/env python

import requests
import os

# 1 get citation information from canlii for cited case
# 2 for each citing case
#   a get text of citing case from canlii
#   b locate citations to cited case
#   c determine paragraph reference
#   d determine sentiment
#   e put into DB

CASEID = "2001scc2"
CANLII_CASE_DATABASE="csc-scc/"
CANLII_BASE_URL = "http://api.canlii.org/v1/"
CANLII_CITATOR = "caseCitator/"
CANLII_LANGUAGE= "en/"

def citing_cases():
  url = CANLII_BASE_URL + CANLII_CITATOR + CANLII_LANGUAGE
  url += CANLII_CASE_DATABASE + CASEID + "/citingCases"
  url += "?api_key=" + CANLII_API_KEY

  r = requests.get(url)
  print(r.headers)

CANLII_API_KEY = os.environ['CANLII_KEY']

citing_cases()
