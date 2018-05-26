import requests

url = ("https://newsapi.org/v2/top-headlines?"
       "country=us&"
       "apiKey=a842f08935ec4c4f8cbfa0ca729fc2c1")

response = requests.get(url)

print ( response.json() )
