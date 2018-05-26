from bs4 import BeautifulSoup
from newsapi import NewsApiClient
import requests

newsapi = NewsApiClient(api_key='a842f08935ec4c4f8cbfa0ca729fc2c1')

def url_gen(str):
    return "https://www.google.com/search?q=" + str.replace(" ", "+") + "&tbm=nws"

def page_scraper(url):
    page = urllib.request.urlopen(url)
    content = BeautifulSoup(page, "html.parser")
    print(content)    

def get_news(search):
    news = newsapi.get_top_headlines(q=search, language="en")
    print(news)

get_news("test")
