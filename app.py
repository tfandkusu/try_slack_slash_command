import os
import json
from flask import Flask
from flask import request
from slack_sdk.signature import SignatureVerifier
import boto3

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        signing_secret = os.environ['TFANDKUSU_SLACK_SIGNING_SECRET']
        timestamp = request.headers['X-Slack-Request-Timestamp']
        signature = request.headers['X-Slack-Signature']
        body = request.get_data().decode('utf-8')
        verifier = SignatureVerifier(signing_secret)
        if verifier.is_valid(body, timestamp, signature):
            name = request.form['text']
            client = boto3.client('lambda')
            client.invoke(
                FunctionName='try-slack-slash-command-dev-worker',
                InvocationType='Event',
                Payload=json.dumps({'name': name}))
            return "Hello %s" % name
        else:
            raise "Verification error"
    else:
        return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, port=4081, host='127.0.0.1')
