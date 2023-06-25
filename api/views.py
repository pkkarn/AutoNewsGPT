from flask import Blueprint, request
from third_parties import news
from langchain.chains import LLMChain
from chain.prompts import headline_summarizer_template
from chain.llm import gpt_model
from third_parties.wordpress.wp import Post
from datetime import date

blue_print = Blueprint('views', __name__)

# Avaialble categories business entertainment general health science sports technology
# Sort of a controller when it compared to node.js
wp_instance = Post()

def post_news_gpt_headlines():
    data = request.get_json()

    if 'category' in data:
        category = data["category"]
        print(category)
        headlines = news.getTopHeadlinesByCategory(category)
        chain = LLMChain(llm=gpt_model(), prompt=headline_summarizer_template)
        final_result = chain.run(headlines=headlines)
        status = wp_instance.create_post({
            "title": "Today's headline {date}".format(date=date.today().strftime('%Y-%m-%d')),
            "content": final_result
        })
        return status
    else:
        raise ValueError("Could not find category")
    

@blue_print.route('/news_gpt/headlines', methods=['POST'])
def news_gpt():
    try:
        return post_news_gpt_headlines()
    except Exception as e:
        return { "error": str(e) }, 400