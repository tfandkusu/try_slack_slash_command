# try_slack_slash_command

Pythonで[SlackのSlack Command](https://api.slack.com/interactivity/slash-commands)を作るための要素技術を確認

## 使用技術

- [AWS Lambda](https://aws.amazon.com/jp/lambda/)
- [Serverless](https://www.serverless.com/)
  - [Serverless Python Requirements](https://github.com/UnitedIncome/serverless-python-requirements)
  - [serverless-wsgi](https://github.com/logandk/serverless-wsgi)
- [Poetry](https://python-poetry.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Python Slack SDK](https://slack.dev/python-slack-sdk/)
- [boto3](https://aws.amazon.com/jp/sdk-for-python/) 時間のかかる処理は別Lambda関数で非同期に処理する。
