from helpers.config import settings, get_settings



class BaseController:
    def __init__(self):
        self.app_settings = get_settings()