from celery import shared_task
import pika

@shared_task
def calculate_expression(expression):
    result = eval(expression)
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='results')
    channel.basic_publish(exchange='', routing_key='results', body=str(result))
    connection.close()
    return result