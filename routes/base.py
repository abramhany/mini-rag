from fastapi import APIRouter
import os 


router = APIRouter(
    prefix='/api/test', ## adds a prefix to all addresses ex : http://localhost:5000/api/test
    tags=['test']
)

@router.get('/')
async def hello():
    app_name = os.getenv('APP_NAME')
    app_version= os.getenv('APP_VERSION')
    return {
        'message':'Hello there!',
        'app_name': app_name,
        'app_version' : app_version,
    }