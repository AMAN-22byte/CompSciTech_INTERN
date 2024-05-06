import pika
from django.conf import settings

def send_message(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASS)
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue='operands')

    channel.basic_publish(exchange='', routing_key='operands', body=message)
    print(" [x] Sent %r" % message)

    connection.close()
