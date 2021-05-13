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
        # App CredentialsのSigning Secretから取得する
        signing_secret = os.environ['TFANDKUSU_SLACK_SIGNING_SECRET']
        # 検証用タイムスタンプ
        timestamp = request.headers['X-Slack-Request-Timestamp']
        # 検証用シグネチャ
        signature = request.headers['X-Slack-Signature']
        # リクエスト本文
        body = request.get_data().decode('utf-8')
        # リクエストを検証する
        verifier = SignatureVerifier(signing_secret)
        if verifier.is_valid(body, timestamp, signature):
            # 検証成功
            name = request.form['text']
            # AWS Lambdaのクライアントを作成
            client = boto3.client('lambda')
            # 非同期でworkerラムダを呼び出す
            # このAPIは3秒以内に返却する必要があるので、時間のかかる処理は別Lambdaで行う
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
