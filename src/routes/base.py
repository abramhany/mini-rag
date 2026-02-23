from fastapi import APIRouter,Depends
import os 
from helpers.config import get_settings ,settings

base_router = APIRouter(
    prefix='/api/v1', ## adds a prefix to all addresses ex : http://localhost:5000/api/test
    tags=['test']
)

@base_router.get('/')
#app_setting :settings makes sure the app_setting is a class
async def hello(app_setting :settings = Depends(get_settings)):# depends make sure the input is available
    app_name = app_setting.APP_NAME
    app_version= app_setting.APP_VERSION
    return {
        'message':'Hello there!',
        'app_name': app_name,
        'app_version' : app_version,
    }