from dbcontext.connection import connection
from src.models import models
import lib.acl as ACL

async def login(user: models.LoginModel):
    result = None
    with connection() as cur:
        cur.execute('call account.user_login(%s, %s, %s)', (user.username, user.password, '{}'))
        result = cur.fetchone()[0]
        print(result)
        if result['status'] == 0:
            result['access_token'] = ACL.access_token(user.username, result['user_id'])
            # set in cookie
            result['refresh_token'] = ACL.refresh_token(user.username, result['user_id'])
    return result

async def registration(user: models.RegistrationModel):
    result = None
    with connection() as cur:
        cur.execute('call account.user_registration(%s, %s, %s, %s, %s)', 
                    (user.first_name, user.last_name, user.login, user.password, '{}'))
        result = cur.fetchone()[0]
    return result

async def save_device(data: models.DeviceTokenModel, payload):
    result = None
    with connection() as cur:
        cur.execute('call account.save_device_token(%s, %s, %s)', 
                    (payload['user_id'], data.dtoken, '{}'))
        result = cur.fetchone()[0]
    return result

async def logout(payload):
    # TODO: delete device token
    pass
