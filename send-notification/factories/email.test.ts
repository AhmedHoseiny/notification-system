import {EmailProvider} from "./email.provider";

describe('Email Provider', () => {
    let provider: any;

    beforeAll(async () => {
        provider = new EmailProvider();
    });

    it('Should send a message', () => {

        const spySend = jest.spyOn(provider, 'send');

        provider.send({
            receivers: ['1', '2', '3']
        });

        expect(spySend).toHaveBeenCalled();
    });
});
