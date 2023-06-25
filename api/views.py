from flask import Blueprint, request
from third_parties import news

blue_print = Blueprint('views', __name__)

# Avaialble categories business entertainment general health science sports technology
# Sort of a controller when it compared to node.js
def post_news_gpt_headlines():
    data = request.get_json()

    if 'category' in data:
        category = data["category"]
        print(category)
        result = news.getTopHeadlinesByCategory(category)
        return result
    else:
        raise ValueError("Could not find category")
    

@blue_print.route('/news_gpt/headlines', methods=['POST'])
def news_gpt():
    try:
        return post_news_gpt_headlines()
    except Exception as e:
        return { "error": str(e) }, 400