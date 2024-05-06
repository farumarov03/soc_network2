# Social main v1 
from fastapi import APIRouter, Depends
from src.models import models
from src.modules import publications, subs, feed
import lib.acl as ACL

router = APIRouter(prefix='/v1')

# region search

@router.get('/search', tags=['search'])
async def find_user(search_text: str, limit: int = 50, offset: int = 50, payload: dict = Depends(ACL.JWTpayload)):
    return await subs.find_user(search_text, limit, offset, payload)

# endregion

# region publication
@router.get('/publication', tags=['publication'])
async def get_user_publication(limit: int = 50, offset: int = 50, payload: dict = Depends(ACL.JWTpayload)):
    return await publications.get_user_publication(limit, offset, payload)

@router.post('/publication', tags=['publication'])
async def create_publication(data: models.PublicationModel, payload: dict = Depends(ACL.JWTpayload)):
    return await publications.create_publication(data, payload)

@router.put('/publication', tags=['publication'])
async def update_publication(data: models.PublicationModel, payload: dict = Depends(ACL.JWTpayload)):
    return await publications.update_publication(data, payload)

@router.delete('/publication', tags=['publication'])
async def delete_publication(id: str, payload: dict = Depends(ACL.JWTpayload)):
    return await publications.delete_publication(id, payload)
# endregion

# region subs

@router.get('/subscribers', tags=['subs'])
async def get_subscribers(limit: int = 50, offset: int = 50, payload: dict = Depends(ACL.JWTpayload)):
    return await subs.get_subscribers(limit, offset, payload)

@router.get('/subscriptions', tags=['subs'])
async def get_subscriptions(limit: int = 50, offset: int = 50, payload: dict = Depends(ACL.JWTpayload)):
    return await subs.get_subscriptions(limit, offset, payload)

@router.post('/subscribe', tags=['subs'])
async def subscribe(to_user_id: str, payload: dict = Depends(ACL.JWTpayload)):
    return await subs.subscribe(to_user_id, payload)

@router.delete('/unsubscribe', tags=['subs'])
async def unsubscribe(sub_id: str, payload: dict = Depends(ACL.JWTpayload)):
    return await subs.unsubscribe(sub_id, payload)

# endregion

# region feed

@router.get('/feed', tags=['feed'])
async def get_feed(limit: int = 50, offset: int = 50, payload: dict = Depends(ACL.JWTpayload)):
    return await feed.get_feed(limit, offset, payload)

# endregion