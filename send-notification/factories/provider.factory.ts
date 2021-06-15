import {ProviderInterface} from "./provider.interface";
import {SmsProvider} from "./sms.provider";
import {FcmProvider} from "./fcm.provider";
import {EmailProvider} from "./email.provider";



const availableProviders: { [key: string]: ProviderInterface } = {
    'sms': new SmsProvider,
    'fcm': new FcmProvider,
    'email': new EmailProvider
};

export class ProviderFactory {

    static create(provider:string) : ProviderInterface {
        const ProviderObject: ProviderInterface = availableProviders[provider];
        return ProviderObject;
    }

}
