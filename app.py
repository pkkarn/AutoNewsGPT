from flask import Flask, request
from api.views import blue_print # sort of router.get

# Define Flask server

app = Flask(__name__)
app.register_blueprint(blue_print , url_prefix='/api')

@app.route("/", methods=["GET"])
def homepage():
    return "It's a homepage"

if __name__ == '__main__':
    app.run(debug=True)

