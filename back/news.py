import requests

def getURL(endpoint, query):
    retURL = "https://newsapi.org/v2/"

    if endpoint != "":
        # endpoint in ["top-headlines", "everything"]
        retURL += endpoint + "?"
    else:
        # default endpoint = "everything"
        retURL += "everything?"

    if query != "":
        retURL += "q=" + query.replace(" ", "+")
    else:
        # default query = "new york city"
        retURL += "q=new+york+city"

    return retURL + "&apiKey=a842f08935ec4c4f8cbfa0ca729fc2c1"


def sourceData(endpoint, query):
    url = getURL(endpoint, query)
    response = requests.get(url)
    return response.json()


## debugging ...


## testing getURL ##


# print ( getURL("", "barack obama") )
# response = requests.get(getURL("","barack obama"))  # should return everything abt B. Obama
# print ( response.json() )

# print ( "#" * 50 )

# print ( getURL("top-headlines", "") )
# response = requests.get(getURL("everything",""))    # should return top headlines abt NYC
# print ( response.json() )

# print ( "#" * 50 )

# print ( getURL("", "") )
# response = requests.get(getURL("everything",""))    # should return everything abt NYC
# print ( response.json() )



## testing getHeadlines


# print ( sourceData("", "barack obama" ) )  # should return everything abt B. Obama
# print ( "#" * 50 )
# print ( sourceData("top-headlines", "") )  # should return top headlines abt NYC
# print ( "#" * 50 )
# print ( sourceData("everything", "")    )  # should return everything abt NYC

