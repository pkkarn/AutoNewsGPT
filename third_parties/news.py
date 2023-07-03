from newsapi import NewsApiClient
from datetime import datetime
import os


today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'

print(today)

news_api_key = os.getenv("NEWS_API")

# Init : https://newsapi.org/docs/client-libraries/python
newsapi = NewsApiClient(api_key=news_api_key)

def getTopHeadlinesByCategory(category: str):
    # input should be one of these: business entertainment general health science sports technology
    print(f'Testing pythong {category}')
    top_headlines = newsapi.get_everything(
                        q="Finance news",
                        language='en',
                        page_size=1,
                        sort_by="publishedAt"
                    )
    
    parsed_headlines = [({
        "url": article['url'],
        # "description": article['description'],
        "title": article['title'],
    }) for article in top_headlines['articles']]
    

    print(parsed_headlines)
    return parsed_headlines;