from pydantic import BaseModel, Field 
from typing import Optional

# region Auth

class LoginModel(BaseModel):
    username: str = Field(..., max_length=20)
    password: str = Field(..., max_length=20)

class RegistrationModel(BaseModel):
    first_name: str = Field(..., max_length=20)
    last_name: str = Field(..., max_length=20)
    login: str = Field(..., max_length=20)
    password: str = Field(..., max_length=20)

class DeviceTokenModel(BaseModel):
    dtoken: str

# endregion


