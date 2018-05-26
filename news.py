#!/usr/bin/python
print("content-type: text/html\n")

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
  <title>OUR PROJECT</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" type="text/css" href="css/Circles.css">
  <link rel="stylesheet" type="text/css" href="css/other.css">
  <style>
  body {
    background-color:#aaf3f4;
  }
.bigbubble0 {
    background-color: white; /* Green */
    border: none;
    color: black;
    padding: 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    height: 500px;
    width: 500px;
    opacity: 0.5;
    position:relative;
    top: 150px;
    left: 25px;
    right: -50px;
    bottom:-50px;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 50%;

}
.bigbubble1 {
    background-color: white; /* Green */
    border: none;
    color: black;
    padding: 20px;
    text-align: center;
    text-decoration: none;
    opacity: 0.5;
    display: inline-block;
    height: 500px;
    width: 500px;
    top: 250px;
    left: 350px;
    right: -75px;
    bottom:-50px;
    position:relative;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 50%;
}

.bigbubble2 {
    background-color: white; /* Green */
    border: none;
    color: black;
    padding: 20px;
    text-align: center;
    text-decoration: none;
    opacity: 0.5;
    display: inline-block;
    height: 500px;
    width: 500px;
    top: 20px;
    left: 400px;
    right: -175px;
    bottom:-150px;
    position:relative;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 50%;
}
.mediumbubble0 {
    background-color: white; /* Green */
    border: none;
    color: black;
    padding: 20px;
    text-align: center;
    text-decoration: none;
    opacity: 0.5;
    display: inline-block;
    height: 350px;
    width: 350px;
    top: 100px;
    left: 400px;
    right: -175px;
    bottom:-150px;
    position:relative;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 50%;
}

.mediumbubble1 {
    background-color: white; /* Green */
    border: none;
    color: black;
    padding: 20px;
    text-align: center;
    text-decoration: none;
    opacity: 0.5;
    display: inline-block;
    height: 350px;
    width: 350px;
    top: 200px;
    left: -850px;
    right: -175px;
    bottom:-150px;
    position:relative;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 50%;
}

.mediumbubble2 {
    background-color: white; /* Green */
    border: none;
    color: black;
    padding: 20px;
    text-align: center;
    text-decoration: none;
    opacity: 0.5;
    display: inline-block;
    height: 350px;
    width: 350px;
    top: -850px;
    left: 525px;
    right: -175px;
    bottom:-150px;
    position:relative;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 50%;
}

.smallbubble0 {
    background-color: white; /* Green */
    border: none;
    color: black;
    padding: 20px;
    text-align: center;
    text-decoration: none;
    opacity: 0.5;
    display: inline-block;
    height: 150px;
    width: 150px;
    top: -525px;
    left: 875px;
    right: -175px;
    bottom:-150px;
    position:relative;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 50%;
}
.smallbubble1 {
    background-color: white; /* Green */
    border: none;
    color: black;
    padding: 20px;
    text-align: center;
    text-decoration: none;
    opacity: 0.5;
    display: inline-block;
    height: 150px;
    width: 150px;
    top: -525px;
    left: -300px;
    right: -175px;
    bottom:-150px;
    position:relative;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 50%;
}
.TINYBUBBLE {
    background-color: white; /* Green */
    border: none;
    color: black;
    padding: 20px;
    text-align: center;
    text-decoration: none;
    opacity: 0.5;
    display: inline-block;
    height: 100px;
    width: 100px;
    top: -605px;
    left: -600px;
    right: -175px;
    bottom:-150px;
    position:relative;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 50%;
}

</style>
</head>
'''

FOOTER = '''
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

        retURL += "q=" + query.replace(" ", "+")

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
        return_dictionary["authors"] = list_of_authors
        return_dictionary["sources"] = list_of_sources
        return_dictionary["urls"] = list_of_urls
        return_dictionary['urlToImage'] = list_of_images

    return return_dictionary

def big_bubble(num):
    dictionary = parse_dictionary()

    url = dictionary["urls"][num]    
    BASE_STRING_START = '<a href="' + url + '" class="bigbubble' + str(num) + ' button' + str(num) + '"> <center><br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>'
    BASE_STRING_END = '</center></a>'

    title = dictionary["titles"][num]
    source = dictionary["sources"][num]
    author = dictionary["authors"][num]
    
    return BASE_STRING_START + "<b>" + title + "</b>\n<br>" + source + "<br>" + author + BASE_STRING_END



def med_bubble(num):
    dictionary = parse_dictionary()

    url = dictionary["urls"][num]    
    BASE_STRING_START = '<a href="' + url + '" class="mediumbubble' + str(num) + ' button' + str(num) + '"> <center><br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>'
    BASE_STRING_END = '</center></a>'

    title = dictionary["titles"][num]
    source = dictionary["sources"][num]
    author = dictionary["authors"][num]
    
    return BASE_STRING_START + "<b>" + title + "</b>\n<br>" + source + "<br>" + author + BASE_STRING_END


def main():
    return_string = ""

    ## generate BIG bubbles
    for i in range(3):
        return_string += big_bubble(i) + "\n\n\t\t"


    ## generate MEDIUM bubbles
    i = 4
    while True:
        try:
            return_string += med_bubble(i) + "\n\n\t\t"
            i += 1
        except:
            break
    
    return_string = return_string.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(r"\uxe9", "'")
    return HEADER + return_string + FOOTER

print(main())
