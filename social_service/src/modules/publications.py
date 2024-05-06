from dbcontext.connection import connection
from src.models import models
import lib.acl as ACL


async def get_user_publication(limit, offset, payload):
    result = None
    with connection() as cur:
        cur.execute('select * from social.get_user_publications(%s, %s, %s)', (payload['user_id'], limit, offset))
        result = cur.fetchone()[0]
    return result


async def create_publication(data: models.PublicationModel, payload):
    result = None
    with connection() as cur:
        cur.execute('call social.create_publication(%s, %s, %s, %s)', 
                    (payload['user_id'], data.post_text, '{}', data.reply_post_id))
        result = cur.fetchone()[0]
    return result


async def update_publication(data: models.PublicationModel, payload):
    result = None
    with connection() as cur:
        cur.execute('call social.update_publication(%s, %s, %s)', 
                    (data.publication_id, data.post_text, '{}'))
        result = cur.fetchone()[0]
    return result


async def delete_publication(id, payload):
    result = None
    with connection() as cur:
        cur.execute('call social.delete_publication(%s, %s)', (id, '{}'))
        result = cur.fetchone()[0]
    return result


