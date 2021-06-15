import {FcmProvider} from "./fcm.provider";

describe('FCM Provider', () => {
    let provider: any;

    beforeAll(async () => {
        provider = new FcmProvider;
    });

    it('Should send a message', () => {

        const spySend = jest.spyOn(provider, 'send');

        provider.send({
            receivers: ['1', '2', '3']
        });

        expect(spySend).toHaveBeenCalled();
    });
});
