# -*- coding: utf-8 -*-
# @Author: adrian
# @Date:   2018-04-07 22:41:21
# @Last Modified by:   Adrian Zucco
# @Last Modified time: 2018-04-08 12:27:22


import json
import requests
import urllib
import nltk
from newspaper import Article
from utils.keywords import filt_keys


def get_key_words(url):

    article = Article(url)
    article.download()
    article.html
    try:
        article.parse()
        article.nlp()
        return article.keywords, article.title, article.publish_date
    except Exception as e:
        return None
    

    


def submit_query(query_words, mode=None, TIMESPAN=None):

    """
    Available modes:
    ToneChart
    WordCloudImageTags
    """
    
    s1 = set(query_words)
    s3 = set.intersection(s1, filt_keys)

    parameters = {"query": " ".join(list(s3)) + ' sourcelang:english', "format": "JSON"}

    print(s3)

    if mode != None:
        parameters["mode"] = mode
        parameters["format"] = "HTML"
    if TIMESPAN != None:
        parameters["TIMESPAN"] = TIMESPAN


    params = urllib.parse.urlencode(parameters, quote_via=urllib.parse.quote)
    response = requests.get("https://api.gdeltproject.org/api/v2/doc/doc", params=params)
    response_json = response.content

    return response_json