# encoding:utf-8
from app.utils.constants import ExchangeType


class Queue:
    """
    class used to create a queue and bind to a callback function.
    """
    def __init__(self):
        """
        initialise the object attribute
        """
        self._rpc_class_list = []

    def __call__(self, queue=None, type=ExchangeType.DEFAULT, exchange='', routing_key=''):
        """
        :param queue:
        :param type:
        :param exchange:
        :param routing_key:
        :return:
        """

        def _(func):
            self._rpc_class_list.append((type, queue, exchange, routing_key, func))

        return _
