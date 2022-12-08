import redis
import json

queue = redis.Redis(charset="utf-8", decode_responses=True)

def pub():
    event = {
        "message": "Welcome to Thamel Remit. Find yourself here",
        "from": "+16506643820",
        "to": "+15719929157"
    }
    queue.publish("broadcast", json.dumps(event))

if __name__ == "__main__":
    pub()