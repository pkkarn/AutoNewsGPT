from newsapi import NewsApiClient
import os

news_api_key = os.getenv("NEWS_API")

# Init : https://newsapi.org/docs/client-libraries/python
newsapi = NewsApiClient(api_key=news_api_key)

def getTopHeadlinesByCategory(category: str):
    top_headlines = newsapi.get_top_headlines(
                        category=category,
                        language='en',
                        country='us'
                    )
    
    parsed_headlines = [({
        "url": article['url'],
        "description": article['description'],
        "author": article['author'],
    }) for article in top_headlines['articles']]
    
    return parsed_headlines;