from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_DB_URL, MONGO_DB_NAME

client = AsyncIOMotorClient(MONGO_DB_URL)
database = client[MONGO_DB_NAME]

def get_database():
    return database