from fastapi import APIRouter, Depends, Body, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from models.notification import Notification
from services.notification_service import NotificationService
from helpers.rabitmq import RabitMQ

notifications_ctrl = APIRouter(tags=["notifications"])


@notifications_ctrl.get('/notifications')
async def get_notifications(_notify_srv: NotificationService = Depends(NotificationService)):
    return await _notify_srv.get_notifications()


@notifications_ctrl.post('/notifications')
async def create_notification(background_tasks: BackgroundTasks, _notify_srv: NotificationService = Depends(NotificationService)
                      , notification: Notification = Body(...), _rabitmq_srv: RabitMQ = Depends(RabitMQ)
                      ):
    notification = jsonable_encoder(notification)
    notification = await _notify_srv.create_notification(notification)    
    background_tasks.add_task(_rabitmq_srv.send_msg, notification_id=notification['id'])
    
    return notification
