import pika
from config import settings


class RabitMQ:
    __rabitmq_conn = None
    _conn_channel = None
    __host = settings.RMQ_HOST
    __queue = settings.RMQ_QUEUE

    def __init__(self):
        self.__init_rabitmq_conn()


    def __init_rabitmq_conn(self):
        if RabitMQ.__rabitmq_conn is None or RabitMQ.__rabitmq_conn.is_closed:
            RabitMQ.__rabitmq_conn = pika.BlockingConnection(pika.ConnectionParameters(self.__host))

    def send_msg(self, notification_id):
        msg = '{"id": "' + str(notification_id) + '"}'
        self._conn_channel = RabitMQ.__rabitmq_conn.channel()
        self._conn_channel.queue_declare(queue = self.__queue)
        self._conn_channel.basic_publish(exchange = '', routing_key = self.__queue, body = msg)
        print(" The Notification '" + str(notification_id) + "' is sent to Queue '" + self.__queue + "'")
        self.__rabitmq_conn.close()
