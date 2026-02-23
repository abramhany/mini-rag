from .BaseController import BaseController
from fastapi import UploadFile
from models import responesSignal

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scaled = self.app_settings.FILE_MAX_SIZE * 1048576
    def validate_uploaded_file(self,file: UploadFile):
        # returns false if the file uploaded is not the same type as the files allowed 
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , responesSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > self.size_scaled:
            return False , responesSignal.FILE_SIZE_EXCEEDED.value
        
        return True , responesSignal.FILE_UPLOAD_SUCCESS.value