from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from controllers import DataController ,ProjectController
from helpers import get_settings , settings
import aiofiles
import logging


logger = logging.getLogger('uvicorn.error')


data_router = APIRouter(
    prefix='/api/v1/data', ## adds a prefix to all addresses ex : http://localhost:5000/api/test
    tags=['api_v1','data']
)
DataController = DataController()
@data_router.post('/upload/{project_id}')
async def upload_data(project_id:str,file:UploadFile,
                      app_setting :settings = Depends(get_settings)):
    


    # validate the file properties
    is_valid,signal = DataController.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal':signal
                }
            
        )
    
    
    try:
        file_path = DataController.generate_unique_filename(file_name=file.filename,project_id=project_id)
        async with aiofiles.open(file_path,'wb') as f:
            while chunk := await file.read(app_setting.FILE_DEFUALT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e :
        
        logger.error(f'Error while uploading file: {e}')
        
        return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'signal':signal
            }
        
    )


    return JSONResponse(
    
        content={
            'signal':signal
            }

    )

