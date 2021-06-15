import {ProviderInterface} from "./provider.interface";
import {NotificationDoc} from "../models/notificationDoc";

const throttledQueue = require('throttled-queue');


export class FcmProvider implements ProviderInterface {
    messageCount = 5;  
    intervalTime = 5 * 1000;

    send(notification: NotificationDoc): void {
        const throttle = throttledQueue(this.messageCount, this.intervalTime);
        const that = this;
        for (let receiver of notification.receivers) {
            throttle(function () {
                notification.receivers = [receiver];
                that.handelMessage(notification);
            });
        }
    }

    private handelMessage(notification: NotificationDoc) {
       
        //  Implementation of provider goes here
        console.log('This notification ' + notification['body'] + ' have been sent by FCM');
    }
}
