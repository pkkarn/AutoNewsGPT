import requests
from bs4 import BeautifulSoup

def get_news_content(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    meta_tags = soup.find_all('meta')

    news_summary = [];

    for meta in meta_tags:
        if 'content' in meta.attrs:
            news_summary.append(meta['content'])


    return ' /n '.join(news_summary)