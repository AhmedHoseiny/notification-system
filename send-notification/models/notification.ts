import mongoose, { Schema } from 'mongoose';
import {NotificationDoc} from "./notificationDoc";

const NotificationSchema: Schema = new Schema({
    providers: { type: Array, required: true },
    body: { type: String, required: true },
    receivers: { type: Array, required: true },
    created_at: { type: String, required: true }
});
export const Notification = mongoose.model<NotificationDoc>('notification', NotificationSchema);

