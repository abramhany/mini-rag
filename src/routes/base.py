from fastapi import APIRouter
import os 
from helpers.config import get_settings

base_router = APIRouter(
    prefix='/api/test', ## adds a prefix to all addresses ex : http://localhost:5000/api/test
    tags=['test']
)

@base_router.get('/')
async def hello():
    app_setting= get_settings()
    app_name = app_setting.APP_NAME
    app_version= app_setting.APP_VERSION
    return {
        'message':'Hello there!',
        'app_name': app_name,
        'app_version' : app_version,
    }