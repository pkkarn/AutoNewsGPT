__all__ = ['headline_summarizer_template']

from langchain import PromptTemplate


headline_prompt = """
    Summarize given news in headlines format, with proper hyperlink, and author.
    Make sure to return in ul li format because its meant for wordpress post.
    Example: `<ul>
    <li><a href="https://www.freightwaves.com/news/teamsters-reject-ups-first-economic-counterproposal" target="_blank" rel="noreferrer noopener">Teamsters union refuses to meet with UPS</a> until a better proposal is made. (Source: Freight Waves by Mark Solomon)</li>
    ...
    </ul>`
     
    Headlines:  \'\'\'\n{headlines}\'\'\'\n Result:
"""

headline_summarizer_template = PromptTemplate(template=headline_prompt, input_variables=["headlines"])