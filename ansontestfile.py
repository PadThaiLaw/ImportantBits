from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import requests

# FIRST STAGE - API call to Canlii, get a list of url's to scrape

# SECOND STAGE - preparing html to more readable text
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

# CORE RUNNING CODE - this will iterate through the current text
def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    for t in visible_texts:
        print(t)
    return u" ".join(t.strip() for t in visible_texts)

# FUN FUNCTIONS
# Find paragraphs
# Derive sentiment score

# html = urllib.request.urlopen('https://www.canlii.org/en/ca/scc/doc/2001/2001scc2/2001scc2.html').read()


CANLII_KEY = "eefjh7g5zneqw33662t5wunu"


# FINAL STAGE - posting to the site, all data should be prepped
def post_to_site(canlii_id, paragraph_num, citation_count, sentiment_sum):
    # Input sample
    # content = {
    #             "canlii_id": "2011scc43",
    #             "citation_count": 39,
    #             "paragraph_num": 71,
    #             "sentiment_sum": -5
    #         }
    content = {
        	"canlii_id": canlii_id,
            "citation_count": citation_count,
            "paragraph_num": paragraph_num,
            "sentiment_sum": sentiment_sum
        }
    request = requests.post("http://importantbits.pythonanywhere.com/api/citation/", json=content)
    print(request.text)
# post_to_site("2007fca198", 15, 25, 2)
# post_to_site("2007fca198", 33, 3, -1)
# post_to_site("2007fca198", 48, 55, 1)
# post_to_site("2007fca198", 100, 4, 5)




# 1 get citation information from canlii for cited case
# 2 for each citing case
#   a get text of citing case from canlii
#   b locate citations to cited case
#   c determine paragraph reference
#   d determine sentiment
#   e put into DB

import requests
import json

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
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    for case in data['citingCases']:
        case['caseId']['en']

CANLII_API_KEY = "eefjh7g5zneqw33662t5wunu"

cc = CanLIIConnection()
cc.citing_cases()



class DjangoModel:
    def __init__(self, canlii_id_str, paragraph_num_int, citation_count_int, sentiment_sum_int):
        self.canlii_id = canlii_id_str
        self.paragraph_num = paragraph_num_int
        self.citation_count = citation_count_int
        self.sentiment_sum = sentiment_sum_int
    def post(self):
        content = {
                "canlii_id": self.canlii_id,
                "citation_count": self.citation_count,
                "paragraph_num": self.paragraph_num,
                "sentiment_sum": self.sentiment_sum
            }
        request = requests.post("http://importantbits.pythonanywhere.com/api/citation/", json=content)
    def increment_count(self):
        self.citation_count += 1
    def set_sentiment(self, new_sentiment):
        self.sentiment = new_sentiment
    def print(self):
        printstring = self.canlii_id + " at paragraph " + str(self.paragraph_num) + ", cited " +str(self.citation_count) + " times and has sentiment score of " + str(self.sentiment_sum)
        print(printstring)


scc = DjangoModel("2001abca23", 33, 25, 5)
scc.post()
scc.print()

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