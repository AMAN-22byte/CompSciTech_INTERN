from django.core.management.base import BaseCommand
import pika
from calculator.utils import *

class Command(BaseCommand):
    help = 'Consumes calculation tasks from the queue'

    def handle(self, *args, **options):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='calculation_tasks')

        def callback(ch, method, properties, body):
            task = body.decode('utf-8')
            operation, operands = task.split(':')
            operands = [int(x) for x in operands.split(',')]
            if operation == 'add':
                result = add(*operands)
            elif operation == 'subtract':
                result = subtract(*operands)
            elif operation == 'multiply':
                result = multiply(*operands)
            elif operation == 'divide':
                result = divide(*operands)
            print(f" [x] Received {task}, Result: {result}")

        channel.basic_consume(queue='calculation_tasks', on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
