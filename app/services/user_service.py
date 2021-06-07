from fastapi import Depends
import datetime
import random
from repositories.user_repository import UserRepository
import string


class UserService:
    def __init__(self, user_repository: UserRepository = Depends(UserRepository)):

        self._user_repo = user_repository

    async def get_users(self):
        return await self._user_repo.get_users()

    async def create_user(self, user: dict) -> dict:
        now = datetime.datetime.now()
        user['token'] = await self._random_string()
        user['created_at'] = now
        return await self._user_repo.create_user(user)

    async def _random_string(self, str_len=70):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(str_len))
