from pydantic_settings import BaseSettings, SettingsConfigDict

# validate and returns the data in the env file
class settings(BaseSettings):
    APP_NAME :str
    APP_VERSION : str
    GOOGLE_API_KEY : str

    class config:
        env_file= '.env'


def get_settings():

    return settings()