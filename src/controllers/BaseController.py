from helpers import get_settings
import os
import string
import random

class BaseController:
    def __init__(self):

        self.app_settings = get_settings()

        
        self.base_dir = os.path.dirname(os.path.dirname(__file__)) # returns the path of the base folder
        self.file_dr = os.path.join(self.base_dir ,
                                    'assets/files')
        
    def generate_randome_name(self,len: int =12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=len))