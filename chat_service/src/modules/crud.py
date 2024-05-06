from dbcontext.connection import connection
from src.models import models
import lib.acl as ACL

async def save_message(from_user, to_user, message):
    result = None
    with connection() as cur:
        cur.execute('call chat.save_message(%s, %s, %s, %s)', (from_user, to_user, message, '{}'))
        result = cur.fetchone()[0]
    return result

async def get_user_contacts():
    pass

