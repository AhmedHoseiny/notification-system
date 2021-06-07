from factories.notification_interface import NotificationInterface


class FcmNotification(NotificationInterface):
    def notify(self, notification: dict):
        # Implementation of provider goes here
        print('This notification ' + notification['body'] + ' have been sent by FCM')
