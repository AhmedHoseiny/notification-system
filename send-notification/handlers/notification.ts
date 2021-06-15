import {Providers} from "./providers";
import {User} from "../models/user";

export class NotificationHandler {

    send(notification: any): Promise<any> {
        const users = this.getUsers(notification.receivers);
        return users.then((users) => {
            notification.receivers = users.map((user: any) => {
                return user.token;
            });
            const providers = new Providers();
            providers.process(notification.providers, notification);
        }).catch(err => {
            console.dir(err);
        });
    }

    private getUsers(ids: Array<string>): Promise<any> {
        return new Promise((resolve, reject) => {
            User.find(
                {
                    _id: {
                        $in: ids
                    }
                },
                {
                    _id: 1,
                    token: 1
                }
            ).then(users => {
                if (!users.length) return reject(Error("User Not Exists"));
                const user = users.map((user) => {
                    return user;
                });
                return resolve(user);

            }).catch()

        })
    }

}
