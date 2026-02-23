from fastapi import FastAPI , APIRouter, Depends, UploadFile
import os
from controllers import DataController 
from helpers.config import get_settings , settings


data_router = APIRouter(
    prefix='/api/v1/data', ## adds a prefix to all addresses ex : http://localhost:5000/api/test
    tags=['api_v1','data']
)

@data_router.post('/upload/{project_id}')
async def upload_data(project_id:str,file:UploadFile,
                      app_setting :settings = Depends(get_settings)):
    is_valid,signal = DataController().validate_uploaded_file(file=file)
    return {
        
        'signal' : signal,
    }
    