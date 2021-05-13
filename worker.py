"非同期でやらせたいタスク"
import time


def handle(event, context):
    print("name = %s" % event['name'])
    time.sleep(5)
    return "Success"
