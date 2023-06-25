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

## Usage

To run this project, execute:

```
python app.py
```