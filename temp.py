from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Now you can access the variables using os.getenv('VARIABLE_NAME')
import os

openai_key = os.getenv("OPENAI_KEY")


"""
PromtTemplate

First try to understand prompt when you use these ai models... Generally, you enter something called prompt.
In chatgpt user can enter anything in their prompt... But in case when you are building an AI application
then you might be using same prompt for all users, but with different parameters.

Prompt 1: Create Sheet of User with username `username` and linkedin `linkedin`.

here username and linkedin are parameters which will be replaced by actual values when user enters their
username and linkedin.

So this the place where you will be defining your prompt template
"""
from langchain import PromptTemplate

from langchain.chat_models import ChatOpenAI  # Wrapper of OpenAI API

"""
Chains: this one will help you to define your chains, that will be doing different tasks, e.g. creating
interacting with different components, external source, talking with other ai agents etc...
"""
from langchain.chains import LLMChain

info = """
    Narendra Damodardas Modi (Gujarati: [ˈnəɾendɾə dɑmodəɾˈdɑs ˈmodiː] (listen); born 17 September 1950)[b] is an Indian politician who has served as the 14th Prime Minister of India since May 2014. Modi was the Chief Minister of Gujarat from 2001 to 2014 and is the Member of Parliament (MP) for Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right-wing Hindu nationalist paramilitary volunteer organisation. He is the longest-serving prime minister from outside the Indian National Congress.
    Modi was born and raised in Vadnagar in northeastern Gujarat, where he completed his secondary education. He was introduced to the RSS at age eight. His account of helping his father sell tea at the Vadnagar railway station has not been reliably corroborated. At age 18, he was married to Jashodaben Modi, whom he abandoned soon after, only publicly acknowledging her four decades later when legally required to do so. Modi became a full-time worker for the RSS in Gujarat in 1971. After the state of emergency was declared by Prime Minister Indira Gandhi in 1975, he went into hiding. The RSS assigned him to the BJP in 1985, and he held several positions within the party hierarchy until 2001, rising to the rank of general secretary.[c]
"""

if __name__ == "__main__":
    print("Hello Langchain!")

    summary_template = """
        Given the linkedin information {information} about person,
        1. create a summary
        2. some cool facts about him.
    """

    try:
        summary_prompt_template = PromptTemplate(
            template=summary_template, input_variables=["information"]
        )
        print(summary_prompt_template)

        llm = ChatOpenAI(
            temperature=0, model="gpt-3.5-turbo", openai_api_key=openai_key
        )

        chain = LLMChain(llm=llm, prompt=summary_prompt_template)

        # item = chain.run(information=info)
        print(openai_key)

    except Exception as e:
        print(f"An error occurred: {e}")

