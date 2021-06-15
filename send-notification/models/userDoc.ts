import { Document } from 'mongoose';


export interface UserDoc extends Document {
    name: string;
    email: string;
    token: string;
    created_at: Date;
}
