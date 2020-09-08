# encoding:utf-8
import pika
import threading

from app.utils.constants import ExchangeType
from .util import logger


class RabbitMQ(object):
    """
    class used to consume message's from rabbitmq
    queue.
    """
    def __init__(self):
        """
        Initialize the variable's used for rabbitmq.
        """
        self.app = None
        self.queue = None
        self.rabbitmq_url = None
        self._connection = None
        self._channel = None

    def init_app(self, app, queue):
        """
        set values in different instance variable's.
        :param app:
        :param queue:
        :return:
        """
        self.app = app
        self.queue = queue
        self.rabbitmq_url = app.config.get('RABBITMQ_URL')
        # initialize some operation
        self.connect_rabbitmq_server()

    # connect RabbitMQ server
    def connect_rabbitmq_server(self):
        """
        method used to connect to rabbitmq server.
        :return: None
        """
        if not self.rabbitmq_url:
            raise Exception("The rabbitMQ application must configure host.")

        self._connection = pika.BlockingConnection(
            pika.URLParameters(self.rabbitmq_url))

        # create channel object
        self._channel = self._connection.channel()

    def temporary_queue_declare(self):
        """
        declare a temporary queue that named random string
        and will automatically deleted when we disconnect the consumer
        :return: the name of temporary queue like amq.gen-4NI42Nw3gJaXuWwMxW4_Vg
        """
        return self.queue_declare(exclusive=True,
                                  auto_delete=True)

    def queue_declare(self, queue_name='test-queue', passive=False, durable=False,
                      exclusive=False, auto_delete=False, arguments=None):
        """
        method used to declare the queue and
        If the queue already exists, no change is made to the queue.
        :param queue_name: the name of the queue which we want to declare.
        :param passive: check whether a queue exists without modifying the server state.
        :param durable: whether the queue is active or not when server restarts.
        :param exclusive: Exclusive queues may only be consumed by the current connection.
        :param auto_delete: the queue is deleted when all consumers have finished using it.
        :param arguments: set of arguments for the declaration of the queue.
        :return:
        """
        result = self._channel.queue_declare(queue=queue_name, passive=passive,
                                             durable=durable, exclusive=exclusive,
                                             auto_delete=auto_delete, arguments=arguments
                                             )
        return result.method.queue

    def exchange_bind_to_queue(self, type, exchange_name, routing_key, queue):
        """
        Declare exchange and bind queue to exchange
        :param type: The type of exchange
        :param exchange_name: The name of exchange
        :param routing_key: The key of exchange bind to queue
        :param queue: queue name
        """
        self._channel.exchange_declare(exchange=exchange_name,
                                       exchange_type=type)
        self._channel.queue_bind(queue=queue,
                                 exchange=exchange_name,
                                 routing_key=routing_key)

    def basic_consuming(self, queue_name, callback):
        """
        method used to define the basic consuming
        :param queue_name:
        :param callback:
        :return: None
        """
        self._channel.basic_consume(queue_name, callback)

    def consuming(self):
        """
        method used to start consuming
        :return: None
        """
        self._channel.start_consuming()

    def _run(self):
        """
        private method to start consuming a queue
        from rabbitmq
        :return:
        """
        # register queues and declare all of exchange and queue
        for (type, queue_name, exchange_name, routing_key, callback) in self.queue._rpc_class_list:

            if type == ExchangeType.DEFAULT:
                if not queue_name:
                    # If queue name is empty, then declare a temporary queue
                    queue_name = self.temporary_queue_declare()
                else:
                    self._channel.queue_declare(queue=queue_name, auto_delete=True)
                    self.basic_consuming(queue_name, callback)

            if type == ExchangeType.FANOUT or type == ExchangeType.DIRECT or type == ExchangeType.TOPIC:
                if not queue_name:
                    # If queue name is empty, then declare a temporary queue
                    queue_name = self.temporary_queue_declare()
                else:
                    self._channel.queue_declare(queue=queue_name)
                self.exchange_bind_to_queue(type, exchange_name, routing_key, queue_name)
                # Consume the queue
                self.basic_consuming(queue_name, callback)

        t = threading.Thread(target=self.consuming)
        logger.info(" * The flask RabbitMQ application is consuming")
        t.setDaemon(True)  # dies when the main thread dies.
        t.start()

    # run the consumer application
    def run(self):
        """
        method used to start the rabbitmq consumer
        :return: None
        """
        self._run()
