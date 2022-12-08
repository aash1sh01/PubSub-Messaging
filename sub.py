import os
import json
from twilio.rest import Client
import redis
from multiprocessing import Process
queue = redis.Redis(charset="utf-8", decode_responses=True)


def sub(test):
    pubsub = queue.pubsub()
    pubsub.subscribe("broadcast")
    print(pubsub.listen())
    for message in pubsub.listen():
        if message.get("type") == "message":
            event = json.loads(message.get("data"))
            print("%s : %s" % (test, event))

            account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
            auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
            body = event["message"]
            from1 = event["from"]
            to = event["to"]
            print(account_sid)
            print(auth_token)
            client = Client(account_sid, auth_token)
            print(client)
            message = client.messages.create(from_=from1, to=to, body=body)
            print(message)
if __name__ == "__main__":
    Process(target=sub, args=("message content",)).start()