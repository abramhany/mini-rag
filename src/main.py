from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from contextlib import asynccontextmanager

from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    db_client = mongo_conn[settings.MONGODB_DATABASE]
    yield {'db_client':db_client}
    mongo_conn.close()

app = FastAPI(lifespan=lifespan)



app.include_router(base.base_router)
app.include_router(data.data_router)

