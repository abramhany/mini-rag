from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

from routes import base



# inzsilze the fastapi
app = FastAPI()

# get the fast api funtion 'router' form 'base' and run it 
app.include_router(base.router)

