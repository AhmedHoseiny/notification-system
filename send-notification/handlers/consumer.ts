import amqp from "amqplib/callback_api";
import {getNotification} from "./message";
import {rabbitmq} from "../config/rabbitmq";


export class Consumer {
    that = this;
    connect() {
        amqp.connect('amqp://' + rabbitmq.host + "", function (error, connection) {
            if (error) {
                throw error;
            }
            connection.createChannel(function (error, channel) {
                if (error) {
                    throw error;
                }
                const queue = rabbitmq.queue;

                channel.assertQueue(queue, {
                    durable: false
                });

                console.log("Waiting messages in %s", queue);
                channel.consume(queue, function (msg) {
                    if (msg) {
                        const message = JSON.parse(msg.content.toString());
                        getNotification(message);
                    }
                }, {
                    noAck: true
                });

            });
        });
    }
}

