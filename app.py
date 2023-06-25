from flask import Flask, request
from api.views import blue_print

# Define Flask server

app = Flask(__name__)
app.register_blueprint(blue_print , url_prefix='/api')

@app.route("/", methods=["GET"])
def homepage():
    return "It's a homepage"

'''
# Todo Tasks:

- [x] create module to handle gpt response
- [ ] create wordpress module to draft posts.
- [ ] Host and Automate this.
- [ ] Get Back and Refactor
'''

if __name__ == '__main__':
    app.run(debug=True)