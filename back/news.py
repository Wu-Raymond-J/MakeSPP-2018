#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi
import cgitb:
import requests
cgitb.enable()

print "content-Type: text/html\n"


def getURL(endpoint, query):
    retURL = "https://newsapi.org/v2/"

    if endpoint != "":
        # endpoint in ["top-headlines", "everything"]
        retURL += endpoint + "?"
    else:
        # default = everything
        retURL += "everything?"

    if query != "":
        retURL += "q=" + query.replace(" ", "+")

    return retURL + "&apiKey=a842f08935ec4c4f8cbfa0ca729fc2c1"


print ( getURL("", "barack obama") )
response = requests.get(getURL("","barack obama"))

print(response.json())
