from .BaseController import BaseController
from fastapi import UploadFile
from models import responesSignal
from .ProjectController import ProjectController
import re
import os

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

    def generate_unique_filename(self,file_name:str,project_id:str):
        
        random_file_name = self.generate_randome_name()
        project_path = ProjectController().get_project_path(project_id=project_id)

        clean_file_name = self.get_clean_file_name(orig_file_name=file_name)


        new_file_path = os.path.join(project_path,
                                     random_file_name+'_'+clean_file_name
                                     )
        while os.path.exists(new_file_path):
            random_file_name = self.generate_randome_name()
            new_file_path = os.path.join(project_path,
                                  random_file_name+'_'+clean_file_name
        )
            return new_file_path
        return new_file_path

    def get_clean_file_name(self,orig_file_name:str):


        cleaned_file_name = re.sub(r'[^\w.]','',orig_file_name.strip())
        

        cleaned_file_name = cleaned_file_name.replace(' ','_')

        return cleaned_file_name
