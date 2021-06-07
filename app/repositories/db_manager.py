from motor.motor_asyncio import AsyncIOMotorClient
import logging
from config import settings
from repositories import db


async def connect_to_mongo():
    logging.info("begin connection...")
    db.client = AsyncIOMotorClient(str(settings.MONGO_URI))[settings.DB_NAME]
    logging.info("database connected！")


async def close_mongo_connection():
    logging.info("disconnecting...")
    db.client.close()
    logging.info("database disconnected！")
