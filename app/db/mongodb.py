from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from typing import Optional

mongodb_client: Optional[AsyncIOMotorClient] = None
mongodb: Optional[AsyncIOMotorClient] = None

async def connect_to_mongo():
    global mongodb_client, mongodb
    mongodb_client = AsyncIOMotorClient(settings.MONGODB_URL)
    mongodb = mongodb_client[settings.MONGODB_NAME]

async def close_mongo_connection():
    global mongodb_client
    if mongodb_client:
        mongodb_client.close()

def get_db() -> AsyncIOMotorClient:
    global mongodb
    if mongodb is None:
        raise ValueError("Database connection is not established.")
    return mongodb
