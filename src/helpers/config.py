from pydantic_settings import BaseSettings, SettingsConfigDict

# validate and returns the data in the env file
class settings(BaseSettings):
    

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    APP_NAME :str
    APP_VERSION : str
    GOOGLE_API_KEY : str
    FILE_ALLOWED_TYPES : list
    FILE_MAX_SIZE : int

    



def get_settings():

    return settings()