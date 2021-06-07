from fastapi import APIRouter, Depends, Body
from services.user_service import UserService
from fastapi.encoders import jsonable_encoder
from models.user import User

users_ctrl = APIRouter(tags=["users"])


@users_ctrl.get('/users')
async def users(_user_srv: UserService = Depends(UserService)):
    return await _user_srv.get_users()


@users_ctrl.post('/users')
async def create_user(_user_srv: UserService = Depends(UserService), user: User = Body(...)):
    user = jsonable_encoder(user)
    user = await _user_srv.create_user(user)
    return user
