# -*- coding: utf-8 -*-
# @Author: adrian
# @Date:   2018-04-07 22:41:21
# @Last Modified by:   Adrian Zucco
# @Last Modified time: 2018-04-07 23:29:23


import json
import requests
import urllib


def submit_query(query_words, mode=None, TIMESPAN=None):

    """
    Available modes:
    ToneChart
    WordCloudImageTags
    """
    
    parameters = {"query": " ".join(query_words), "format": "JSON"}

    if mode != None:
        parameters["mode"] = mode
        parameters["format"] = "HTML"
    if TIMESPAN != None:
        parameters["TIMESPAN"] = TIMESPAN


    params = urllib.parse.urlencode(parameters, quote_via=urllib.parse.quote)
    response = requests.get("https://api.gdeltproject.org/api/v2/doc/doc", params=params)
    response_json = response.content

    return response_json