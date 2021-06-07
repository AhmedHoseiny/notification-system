from fastapi import Depends
from repositories import AsyncIOMotorClient, get_database
from motor.motor_asyncio import AsyncIOMotorClient
from models.notification import notification_dict


class NotificationRepository:
    def __init__(self, db: AsyncIOMotorClient = Depends(get_database)):
        self._db = db

    async def get_notifications(self):
        notifications = []
        async for notification in self._db['notifications'].find():
            notifications.append(notification_dict(notification))
        return notifications

    async def create_notification(self, notification: dict) -> dict:
        row = await self._db['notifications'].insert_one(notification)
        notification = await self._db['notifications'].find_one({"_id": row.inserted_id})
        return notification_dict(notification)
