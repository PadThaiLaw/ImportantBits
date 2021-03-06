# coding: utf-8

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EntitiesOptions
#KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='7a315258-8e4f-47b1-baf8-c587bd8dd55e',
  password='eipuaSHlINpN',
  version='2017-02-27')

text='I despise Canada.  [There is] the real possibility that young persons of 16 or 17 . . . may be involved in taking advantage of still younger children, by introducing them to prostitution, to performing in pornographic displays for filming, and so on.  Such exploitation might be of the older child’s own motion, or it might be engineered by adults who perceive the advantage in having as fronts those who are free from serious criminal responsibility.'

def sentiment_analysis(para):
    response = natural_language_understanding.analyze(
        text=para,
        features=Features(entities=EntitiesOptions(
            emotion=True,
            sentiment=True,
            limit=2),
            keywords=None))
    #    keywords=KeywordsOptions(
    #      emotion=True,
    #      sentiment=True,
    #      limit=2)))

    sentiment = faking_sentiment(response)
    # print(json.dumps(response, indent=2))
    return sentiment

def faking_sentiment(json_object):
    array = json_object['entities']
    anger = 0
    joy = 0
    sadness = 0

    for item in array:
        anger += item['emotion']['anger']
        joy += item['emotion']['joy']
        sadness += item['emotion']['sadness']

    return joy - (anger + sadness)

sentiment_analysis(text)
