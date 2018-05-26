from newsapi import NewsApiClient

newsapi = api.NewsApiClient(api_key='a842f08935ec4c4f8cbfa0ca729fc2c1')

def get_news(search):
    news = newsapi.get_top_headlines(q=search, language="en")
    print(news)

get_news("test")
