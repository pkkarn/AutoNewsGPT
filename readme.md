### AutoNewsGPT

**Description**: Idea to make this app, which will aggregate latest news from NEWS API and write headlines using that...

**Features**

- It uses `OpenAI` to summarize top headlines,
- Will use `Langchain` to manage multi level prompting
- `Wordpress` API to draft generated content
- Flask has been used to shoot up quick server

![Screenshot](./Screenshot.png)


### Installation

Follow these steps to run this project on your local machine.

1. Clone this repository:
    ```
    git clone https://github.com/pkkarn/AutoNewsGPT.git
    ```

2. Navigate to the project directory:
    ```
    cd AutoNewsGPT
    ```

3. Set up a Python virtual environment:

    Unix/MacOS:
    ```
    python3 -m venv env
    source env/bin/activate
    ```
    Windows:
    ```
    py -m venv env
    .\env\Scripts\activate
    ```

4. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```


5. Add .env file at root level.

```
OPENAI_KEY="sk-xxx"
NEWS_API="xxx" # Get API Key: https://newsapi.org/docs/client-libraries/python
```

## Usage

To run this project, execute:

```
python app.py
```


## API Endpoints

1. Get news by category:

**Body**

```
router: /api/news_gpt/headlines

body: {
    "category": "business"
}
```

**Response**

```
[
    {
        "author": "Faye Prosser",
        "description": "A recall has been issued for multiple frozen fruit products and fruit blends due to possible Listeria monocytogenes contamination. Multiple grocery stores nationwide are included in this recall (incl. NC).",
        "url": "https://www.wral.com/story/frozen-fruit-recall-due-to-possible-listeria-contamination/20923691/"
    },
    {
        "author": "Kristen Altus",
        "description": "Debbie, Jennifer, Sheryl and Wendy Yuengling say the secret to their sixth-generation success at America's oldest brewery comes from their \"proud,\" patriotic family bond.",
        "url": "https://www.foxbusiness.com/business-leaders/americas-oldest-brewery-reminds-beer-lovers-story-nobody-else"
    },
    ...
]
```

