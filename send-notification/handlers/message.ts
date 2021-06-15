import {Notification} from "../models/notification";
import {NotificationHandler} from "./notification";


export const getNotification = (message: any) => {
    Notification.findOne({_id: message.id})
        .then(notification => {
            if (notification) {
                const notificationHandler = new NotificationHandler();
                notificationHandler.send(notification);
            }
        })
        .catch(err => {throw new Error('no notification found')});
};
