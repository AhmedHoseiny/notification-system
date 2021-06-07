from fastapi import Depends
from factories.providers.email_notification import EmailNotification
from factories.providers.fcm_notification import FcmNotification
from factories.providers.sms_notification import SmsNotification


class NotificationFactory:
    def __init__(self, email_notification: EmailNotification = Depends(EmailNotification),
                 fcm_notification: FcmNotification = Depends(FcmNotification),
                 sms_notification: SmsNotification = Depends(SmsNotification)
                 ):
        self._notify_by_email = email_notification
        self._notify_by_fcm = fcm_notification
        self._notify_by_sms = sms_notification

    def send(self, notification: dict):
        for provider in notification['providers']:
            if provider == 'sms':
                return self._notify_by_email.notify(notification)
            elif provider == 'fcm':
                return self._notify_by_fcm.notify(notification)
            elif provider == 'email':
                return self._notify_by_email.notify(notification)
            else:
                return 'invalid'
