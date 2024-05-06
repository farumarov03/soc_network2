from dbcontext.connection import connection
from src.models import models
import lib.acl as ACL

# лента
async def get_feed(limit, offset, payload):
    result = None
    with connection() as cur:
        cur.execute('select * from social.get_publications_feed(%s, %s, %s)', (payload['user_id'], limit, offset))
        result = cur.fetchone()[0]
    return result