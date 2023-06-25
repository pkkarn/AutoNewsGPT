from newsapi import NewsApiClient
import os

news_api_key = os.getenv("NEWS_API")

# Init : https://newsapi.org/docs/client-libraries/python
newsapi = NewsApiClient(api_key=news_api_key)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(
                                          category='business',
                                          language='en',
                                          country='us')

item = [({
    "url": article['url'],
    "description": article['description'],
    "author": article['author'],
}) for article in top_headlines['articles']]

print(item)

# test_url = [{'url': 'https://www.yahoo.com/lifestyle/amazon-sale-airpods-214550557.html'}, {'url': 'https://www.bloomberg.com/news/articles/2023-06-24/gloom-returns-to-china-markets-as-stimulus-trade-fizzles-out'}, {'url': 'https://www.reuters.com/markets/deals/spacex-tender-offer-values-company-about-150-billion-bloomberg-news-2023-06-23/'}, {'url': 'https://www.mmamania.com/2023/6/23/23771318/ufc-champion-jon-jones-offers-to-train-mark-zuckerberg-for-elon-musk-fight-dana-white-meta-twitter'}, {'url': 'https://6abc.com/baby-shark-recall-bath-toys-cuts/13419336/'}, {'url': 'https://www.reuters.com/markets/us/futures-fall-powells-hawkish-stance-sours-market-mood-2023-06-23/'}, {'url': 'https://www.youtube.com/watch?v=_DiGjp0xo0E'}, {'url': 'https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-market-pullback-healthy-as-apple-hits-record-high-what-to-do/'}, {'url': 'https://www.usatoday.com/story/news/health/2023/06/23/fda-approves-hair-loss-drug-for-teens-12-and-up/70345863007/'}, {'url': 'https://www.statnews.com/2023/06/23/lillys-obesity-pill-cuts-15-of-weight-at-highest-dose-in-mid-stage-trial/'}, {'url': 'https://www.wmur.com/article/fda-new-hampshire-retailers-flavored-vape/44321963'}, {'url': 'https://www.freep.com/story/money/cars/2023/06/23/uaw-blasts-biden-administration-over-ford-sk-battery-loan/70351845007/'}, {'url': 'https://www.foodsafetynews.com/2023/06/more-frozen-fruit-recalled-over-listeria-concerns/'}, {'url': 'https://www.staradvertiser.com/2023/06/23/breaking-news/carlos-ghosn-says-1b-lawsuit-against-nissan-is-reasonable/'}, {'url': 'https://news.yahoo.com/buttigieg-warns-airlines-finish-retrofitting-202321830.html'}, {'url': 'https://www.foxbusiness.com/markets/bitcoin-faithful-embrace-31000-level-new-high'}, {'url': 'https://www.sfgate.com/tech/article/halle-berry-sf-tech-executive-18167943.php'}, {'url': 'https://www.youtube.com/watch?v=lJrWiH0r2CQ'}, {'url': 'https://abc13.com/ercot-weather-watch-electricity-demand-texas-hot/13419181/'}, {'url': 'https://www.freightwaves.com/news/teamsters-reject-ups-first-economic-counterproposal'}]
# print(test_url)

# for urlObj in test_url:
#     print(urlObj['content'])

# final_result = [(news_content.get_news_content(url=urlObj['url'])) for urlObj in test_url]
# print(final_result)