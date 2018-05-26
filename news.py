#!/usr/bin/python
print( "Content-type: text/html\n")
import cgitb
cgitb.enable()

import cgi
import requests
import json

form = cgi.FieldStorage()

print ('''
<!DOCTYPE html>
<html>

<head>
  <title>Project Name</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" type="text/css" href="css/other.css">
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="stylesheet" type="text/css" href="css/bubbles.css">

</head>

<body>
  <div class="bgimg w3-display-container w3-animate-opacity w3-text-white">
    <div class="w3-display-topleft w3-padding-large w3-xlarge">
      Logo
    </div>
    <div class="w3-display-middle">
    <a href="www.google.com" class="button">Link Button</a>
    </div>


    <div class="w3-display-bottomleft w3-padding-large">
      Rubin Peci, Kaitlin Wan, Raymond Wu, Anne Zhang
    </div>
  </div>
 <ul class="bg-bubbles">
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>

<ul>

</body>

</html>
''')

def getURL(endpoint, query):
    retURL = "https://newsapi.org/v2/"

    if endpoint != "":
        # endpoint in ["top-headlines", "everything"]
        retURL += endpoint + "?"
    else:
        # default endpoint = "top-headlines"
        retURL += "top-headlines?"

    if query != "":
        retURL += "q=" + query.replace(" ", "+")
    else:
        # default query = "new york city"
        retURL += "q=new+york+city"

    return retURL + "&apiKey=a842f08935ec4c4f8cbfa0ca729fc2c1"


## returns JSON dictionary...
def sourceData(endpoint, query):
    url = getURL(endpoint, query)
    response = requests.get(url)
    data = response.json()
    return data


json = sourceData("", "")
for key, value in json.items():
    if key == "articles":
        print (key)
        print ("****")
        for thing in value:
            print (thing )
            print ( "\n\n" )
        print ("****")
    else:
        print (key, value)


def parseFormData():
    endpoint = ""   # temporary
    # endpoint = form.getValue('endpoint')
    query = form.getvalue('search')

    return sourceData(endpoint, query)

