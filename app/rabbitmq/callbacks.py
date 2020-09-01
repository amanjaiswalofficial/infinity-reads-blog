from app import queue


@queue(queue='blog-queue', type='direct', exchange='blog-exchange', routing_key='blog-key')
def blog_queue(ch, method, props, body):
    print("simple queue => {}".format(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)  # for acknowledgement

