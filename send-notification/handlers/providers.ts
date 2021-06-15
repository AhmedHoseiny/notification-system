import {NotificationDoc} from "../models/notificationDoc";
import {ProviderFactory} from "../factories/provider.factory";

export class Providers {
    process(providers: Array<string>, notification: NotificationDoc): void {
        if (providers.length > 0) {
            for (let provider of providers) {
                const providerObject = ProviderFactory.create(provider);
                if (providerObject) {
                    providerObject.send(notification);
                }
            }
        }
    }
}
