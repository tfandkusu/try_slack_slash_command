from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        # TODO リクエストの検証を行う
        return "Hello %s" % request.form['text']
    else:
        return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, port=4081, host='127.0.0.1')
