import mongoose, { Schema } from 'mongoose';
import {UserDoc} from "./userDoc";

const UserSchema: Schema = new Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    token: { type: String, required: true },
    created_at: { type: String, required: true }
});
export const User =  mongoose.model<UserDoc>('User', UserSchema);
