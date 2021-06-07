from fastapi import Depends
import datetime
import random
import string
from repositories.notification_repository import NotificationRepository
from factories.notification_factory import NotificationFactory


class NotificationService:
    def __init__(self, notification_repository: NotificationRepository = Depends(NotificationRepository),
                 notification_factory: NotificationFactory = Depends(NotificationFactory)):
        self._notify_repo = notification_repository
        self._notify_factory = notification_factory

    async def get_notifications(self):
        return await self._notify_repo.get_notifications()

    async def create_notification(self, notification: dict) -> dict:
        now = datetime.datetime.now()
        notification['created_at'] = now
        return await self._notify_repo.create_notification(notification)

    async def _random_string(self, str_len=70):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(str_len))

    def send_notification(self, notification: dict):
        return self._notify_factory.send(notification)
