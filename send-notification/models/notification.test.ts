import {Database} from "../database";
import {Notification} from './notification';
import {NotificationDoc} from "./notificationDoc";

describe('Notification model', () => {
    let db: Database;

    beforeAll(async () => {
        db = new Database;
        await db.connect();
    });

    afterAll(async () => {
        db.close();
    });

    it('Should throw validation errors', () => {
        const notification = new Notification();

        expect(notification.validate).toThrow();
    });

    it('Should save a notification', async () => {
        const notification: NotificationDoc = new Notification({
            providers: ['sms', 'fcm'],
            body: 'dummy body',
            receivers: ['topic_name'],
            created_at: 'dummy date',
        });
        const spySave = jest.spyOn(notification, 'save');
        notification.save();
        expect(spySave).toHaveBeenCalled();

        expect(notification).toMatchObject({
            providers: expect.any(Array),
            body: expect.any(String),
            receivers: expect.any(Array),
            created_at: expect.any(String),
        });

        expect(notification.providers).toEqual(expect.arrayContaining(['sms', 'fcm']));
        expect(notification.body).toBe('dummy body');
    });
});
