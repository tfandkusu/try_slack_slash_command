from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/cats")
def cats():
    return "Cats"


if __name__ == "__main__":
    app.run(debug=True, port=4081, host='127.0.0.1')
