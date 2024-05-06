# Auth main 
from fastapi import APIRouter, Depends
from src.models import models
from src.modules import autorization
import lib.acl as ACL

router = APIRouter(prefix='/v1', tags=["Auth V1"])

@router.post('/login')
async def login(data: models.LoginModel):
    return await autorization.login(data)

@router.post('/registration')
async def registration(data: models.RegistrationModel):
    return await autorization.registration(data)

# save device token for push notifications
@router.post('/device_token')
async def save_device(data: models.DeviceTokenModel, payload: dict = Depends(ACL.JWTpayload)):
    return await autorization.save_device(data, payload)

@router.post('/logout')
async def logout(payload: dict = Depends(ACL.JWTpayload)):
    return await autorization.logout(payload)

