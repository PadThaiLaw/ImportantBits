# IMPORTS
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import requests
import json
import os

# starting point CanLII params
CASEID = "2017fca8"
CANLII_CASE_DATABASE="fca/"

# CanLII constants
CANLII_BASE_URL = "http://api.canlii.org/v1/"
CANLII_CITATOR = "caseCitator/"
CANLII_BROWSE = "caseBrowse/"
CANLII_LANGUAGE= "en/"

# get environment variables
# TODO: CANLII_API_KEY = os.environ['CANLII_KEY']
CANLII_API_KEY = "eefjh7g5zneqw33662t5wunu"

# GLOBAL VARIABLES
# List of CitingCase objects of all cases that cite
citing_cases = []
# Format, list of a list [[23,0.5], [25,0.6], [23,-1]]
aggregate_data = []
# Format, list of APIModel objects
citations_list = []

# CLASSES
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
    # Print in reader friendly
    def print(self):
        printstring = self.canlii_id + " at paragraph " + str(self.paragraph_num) + ", cited " +str(self.citation_count) + " times and has sentiment score of " + str(self.sentiment_sum)
        print(printstring)

class CitingCase:

  def __init__(self):
    self.caseId = ""
    self.truncated_title = ""
    self.databaseId = ""
    self.url = ""

class CanLIIConnection:

  def citing_cases(self):
    url = CANLII_BASE_URL + CANLII_CITATOR + CANLII_LANGUAGE
    url += CANLII_CASE_DATABASE + CASEID + "/citingCases"
    url += "?api_key=" + CANLII_API_KEY

    r = requests.get(url)
    body = json.loads(r.text)
    array = body['citingCases']

    for item in array:
      self.build_citing_case(item)
      # print(item['caseId']['en'])

  def build_citing_case(self, case_object):
    url = CANLII_BASE_URL + CANLII_BROWSE + CANLII_LANGUAGE
    url += case_object['databaseId'] + "/" + case_object['caseId']['en']
    url += "?api_key=" + CANLII_API_KEY

    r = requests.get(url)
    body = json.loads(r.text)
    case_url = body['url']
    truncated_title = body['title'].split()[0]

    tmp = CitingCase()
    tmp.caseId = case_object['caseId']['en']
    tmp.truncated_title = truncated_title
    tmp.databaseId = case_object['databaseId']
    tmp.url = case_url
    citing_cases.append(tmp)
    print("Queuing: " + tmp.truncated_title + " (" + tmp.caseId + ")" + " at " + tmp.url)

# HELPER FUNCTIONS
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def sentiment_analysis(text):
    return -0.5

def find_paragraphs(text):
    if "para" in text:
        return [13, 23]
    else:
        return None

# Process ONE webpage
def process_html(url):
    body = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    for t in visible_texts:
        paragraph_list = find_paragraphs(t)
        if paragraph_list:
            sentiment_score = sentiment_analysis(t)
            for para in paragraph_list:
                aggregate_data.append([para, sentiment_score])

# Loop over list of webpages
def loop_over_htmls(list_of_html):
    for html in list_of_html:
        print("Currently parsing " + html)
        process_html(html)

# POST PROCESSING
# Sort and combine aggregate data list
def process_aggregate_data(local_agg_data, canlii_id):
    # Input format, list of a list [[23,0.5], [25,0.6], [23,-1]]
    local_agg_data.sort(key=lambda x: x[0]) # Sorts the list of list based on value at index[0]
    # Initialize parameters
    current_paragraph = None
    current_count = 0
    current_sentiment_score = 0
    # Parameters for counting, to action at the final pair of data
    index = 0
    length_agg_data = len(local_agg_data)

    # Loop over each pair in a sorted list, if they are the same paragraph, increment count and add sentiments, otherwise save to model list
    for pair in local_agg_data:
        index += 1
        if pair[0] != current_paragraph:
            if (current_count != 0) or (index==length_agg_data):
                print([current_paragraph, current_count, current_sentiment_score])
                # TODO Save as model to model list
                # citations_list.append(APIModel(canlii_id, current_paragraph, current_count, current_sentiment_score))
            current_paragraph = pair[0]
            current_count = 1
            current_sentiment_score = pair[1]
        else:
            current_count += 1
            # TODO: Determine what our algorithm is
            current_sentiment_score = current_sentiment_score + pair[1]
        # Catches the last paragraph that will not switch
        if index==length_agg_data:
            print([current_paragraph, current_count, current_sentiment_score])
            # TODO Save as model to model list
            # citations_list.append(APIModel(canlii_id, current_paragraph, current_count, current_sentiment_score))


# RUN TIME CODE:

def run_script():
    # Getting a URL List to iterate through
    cc = CanLIIConnection()
    cc.citing_cases()
    url_list = []
    for case in citing_cases:
        url_list.append(case.url)
    # Loop over HTMLs
    loop_over_htmls(url_list)
    # Process aggregate data which will post to website
    process_aggregate_data(aggregate_data, CASEID)
    
run_script()
