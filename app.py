from flask import Flask, request

# Define Flask server

app = Flask(__name__)

def handle_post():
    data = request.get_json()
    topic, search = data["topic"], data["search"]

    result = { "topic": topic, "search": search }
    return result

@app.route("/api/news_gpt", methods=["POST"])
def getNews():
    return handle_post()

if __name__ == '__main__':
    app.run(debug=True)

