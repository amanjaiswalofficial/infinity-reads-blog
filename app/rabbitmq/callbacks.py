from app import queue


@queue(queue='blog-queue', type='direct', exchange='blog-exchange', routing_key='blog-key')
def blog_queue(ch, method, props, body):
    """
    declare the queue of direct exchange, flask-rabbitmq will bind automatically by key.
    :param ch:
    :param method:
    :param props:
    :param body:
    :return:
    """
    print("simple queue => {}".format(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)  # for acknowledgement

