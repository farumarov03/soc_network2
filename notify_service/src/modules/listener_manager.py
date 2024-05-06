import redis
import json
from lib.config import redis_config
import asyncio

conn = redis_config()
CHANEL = 'SUB_EVENTS'

async def send_push_notification(data):
    await asyncio.sleep(5)
    print("send notification: ", data)
    # TODO: Get user device tokens
    # TODO: Send notification, use Firebase and FCM lib

events = {
    "1": send_push_notification
    # For another functions by event types
}

def redis_listener():
    r = redis.Redis(host=conn['host'], port=conn['port'], db=0)
    pubsub = r.pubsub()
    pubsub.subscribe(CHANEL)
    for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            event_type = data.get('type')
            if event_type in events:
                asyncio.run(events[event_type](data))
            else:
                print(f"No function found {event_type}")


