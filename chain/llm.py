from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI  # Wrapper of OpenAI API

load_dotenv()  # take environment variables from .env.
# Now you can access the variables using os.getenv('VARIABLE_NAME')
import os

openai_key = os.getenv("OPENAI_KEY")


def gpt_model():
    llm = ChatOpenAI(
            temperature=0, 
            model="gpt-3.5-turbo", 
            openai_api_key=openai_key
        )
    
    return llm