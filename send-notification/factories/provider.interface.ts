import {NotificationDoc} from "../models/notificationDoc";

export  interface ProviderInterface {
     messageCount: number;   //request per time
     intervalTime: number;   //minute;
     send(notification: NotificationDoc): void;
}
