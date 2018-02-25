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

CASEID = "2007fca198"
CANLII_CASE_DATABASE="csc-scc/"
CANLII_BASE_URL = "http://api.canlii.org/v1/"
CANLII_CITATOR = "caseCitator/"
CANLII_LANGUAGE= "en/"

class CanLIIConnection:

  def citing_cases(self):
    url = CANLII_BASE_URL + CANLII_CITATOR + CANLII_LANGUAGE
    url += CANLII_CASE_DATABASE + CASEID + "/citingCases"
    url += "?api_key=" + CANLII_API_KEY

    r = requests.get(url)

CANLII_API_KEY = os.environ['CANLII_KEY']

cc = CanLIIConnection()
cc.citing_cases()
