from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from .llm import gpt_model
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain.docstore.document import Document
from third_parties import news
from langchain.chains.summarize import load_summarize_chain
load_dotenv()

import os
import requests
from bs4 import BeautifulSoup


os.environ["SERPAPI_API_KEY"]
openai_api_key = os.environ["OPENAI_KEY"]



llm = OpenAI(temperature=0, model="text-davinci-003", openai_api_key=openai_api_key, max_tokens=1000)

chain = load_summarize_chain(llm, chain_type="map_reduce")

def summarize (url):
    try:
        print(url)
        r = requests.get(url)
        # Create an instance of the BeautifulSoup class to parse our webpage
        soup = BeautifulSoup(r.text, 'html.parser')

        # Use the BeautifulSoup 'find' function to find all the sections in the webpage
        sections = soup.find_all('article')

        newsContent = ''
        # Iterate over the sections and print them
        for section in sections:
            newsContent += section.get_text()

        words = newsContent.split()

        # Fix this issue: which is you have split and send token within limiation

        print(words)
        
        docs = [Document(page_content=t) for t in words[:1000]]

        summarized_news = chain.run(docs)

        return summarized_news
    except Exception as e:
        print(e)

tools = [Tool(
    name="search_news",
    description="useful when you want to search latest news, input should be string",
    func=news.getTopHeadlinesByCategory
), Tool(
    name="summarizer",
    description="To summarize news, input should be news url in string",
    func=summarize
)]


# tools = load_tools(tools, llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)