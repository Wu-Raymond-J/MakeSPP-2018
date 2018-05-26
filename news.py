#!/usr/bin/python
print( "Content-type: text/html\n")
import cgitb
cgitb.enable()

import cgi
import requests
import json

form = cgi.FieldStorage()

HEADER = '''
<!DOCTYPE html>
<html>

<head>
  <title>MAKESPP 2018</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" type="text/css" href="css/other.css">
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="stylesheet" type="text/css" href="css/bubbles.css">

</head>

<body>
  <div class="bgimg w3-display-container w3-animate-opacity w3-text-white">
    <div class="w3-display-topleft w3-padding-large w3-xlarge">
      MAKESPP 2018
    </div>

'''

FOOTER = '''
    <div class="w3-display-bottomleft w3-padding-large">
      Rubin Peci, Kaitlin Wan, Raymond Wu, Anne Zhang
    </div>
  </div>

</body>

</html>'''

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

def parseFormData():
    endpoint = ""   # temporary
    # endpoint = form.getValue('endpoint')
    query = form.getvalue('search')
    #### TEMPORARY
    query = "new york city"
    json = sourceData(endpoint, query)
    return json

'''    for key, value in json.items():
    if key == "articles":
        print (key)
        print ("****")
        for thing in value:
            print (thing )
            print ( "\n\n" )
        print ("****")
    else:
        print (key, value)
'''

def parse_dictionary():
    dictionary = parseFormData()
    return_dictionary = {}

    list_of_titles = []
    list_of_authors = []
    list_of_sources= []
    list_of_urls = []
    list_of_images = []

    if int(dictionary["totalResults"]) == 0:
        print("No relevant articles found!")
    else:
        articles = dictionary["articles"]
        for article in articles:
            list_of_titles.append(article["title"])
            list_of_authors.append(article["author"])
            list_of_sources.append(article['source']['name'])
            list_of_urls.append(article['url'])
            list_of_images.append(article['urlToImage'])

        return_dictionary["titles"] = list_of_titles
        return_dictionary["author"] = list_of_authors
        return_dictionary["sources"] = list_of_sources
        return_dictionary["urls"] = list_of_urls
        return_dictionary['urlToImage'] = list_of_images

    return return_dictionary

def big_bubble(num):
    dictionary = parse_dictionary()

    url = dictionary["urls"][num]    
    BASE_STRING_START = '<a href="' + url + '" class="bigbubble' + str(num) + ' button' + str(num)
    BASE_STRING_END = '</a>'

    title = dictionary["titles"][num]
    source = dictionary["sources"][num]
    author = dictionary["authors"][num]
    
    return BASE_STRING_START + "<b>" + title + "</b>\n<br>" + source + "<br>" + author + BASE_STRING_END

def main():
    return_string = ""
    for i in range(3):
        return_string += bubble(i) + "\n\n\t\t"

    return HEADER + return_string + FOOTER

print(main())
