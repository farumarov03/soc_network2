import redis
from lib.config import redis_config

conn = redis_config()

async def publish_event(channel, message):
    r = redis.Redis(host=conn['host'], port=conn['port'], decode_responses=True)
    r.publish(channel, message)


