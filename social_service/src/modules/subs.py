from dbcontext.connection import connection
from dbcontext.redis_manager import publish_event
import json

CHANEL = 'SUB_EVENTS'

async def find_user(search_text, limit, offset, payload):
    result = None
    with connection() as cur:
        cur.execute('select * from social.search_users(%s, %s, %s, %s)', (search_text, payload['user_id'], limit, offset))
        result = cur.fetchone()[0]
    return result

async def get_subscribers(limit, offset, payload):
    result = None
    with connection() as cur:
        cur.execute('select * from social.get_user_subscribers(%s, %s, %s)', (payload['user_id'], limit, offset))
        result = cur.fetchone()[0]
    return result

async def get_subscriptions(limit, offset, payload):
    result = None
    with connection() as cur:
        cur.execute('select * from social.get_user_subscriptions(%s, %s, %s)', (payload['user_id'], limit, offset))
        result = cur.fetchone()[0]
    return result

async def subscribe(to_user_id, payload):
    result = None
    with connection() as cur:
        cur.execute('call social.subscribe_to_user(%s, %s, %s)', (payload['user_id'], to_user_id, '{}'))
        result = cur.fetchone()[0]
        if result['status'] == 1:
            # publish event to redis chanel for notify service
            await publish_event(CHANEL, json.dumps({"type": "1", "name": "subscribe", "send_to": to_user_id}))
    return result

async def unsubscribe(sub_id, payload):
    result = None
    with connection() as cur:
        cur.execute('call social.unsubscribe_from_user(%s, %s, %s)', (payload['user_id'], sub_id, '{}'))
        result = cur.fetchone()[0]
    return result