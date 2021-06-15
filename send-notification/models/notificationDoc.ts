import { Document } from 'mongoose';


export interface NotificationDoc extends Document {
    providers: string[];
    body: string;
    receivers: string[];
    created_at: Date;
}
