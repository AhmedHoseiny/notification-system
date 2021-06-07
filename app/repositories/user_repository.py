from fastapi import Depends
from repositories import AsyncIOMotorClient, get_database
from motor.motor_asyncio import AsyncIOMotorClient
from models.user import user_dict


class UserRepository:
    def __init__(self, db: AsyncIOMotorClient = Depends(get_database)):
        self._db = db

    async def get_users(self):
        users = []
        async for user in self._db['users'].find():
            users.append(user_dict(user))
        return users

    async def create_user(self, user: dict) -> dict:
        row = await self._db['users'].insert_one(user)
        user = await self._db['users'].find_one({"_id": row.inserted_id})
        return user_dict(user)
