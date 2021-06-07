from fastapi import APIRouter

from api.controllers.users_controller import users_ctrl
from api.controllers.notifications_controller import notifications_ctrl

router = APIRouter()

router.include_router(users_ctrl)
router.include_router(notifications_ctrl)
