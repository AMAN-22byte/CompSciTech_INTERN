from django.core.management.base import BaseCommand
import pika
import json
import os

class Command(BaseCommand):
    help = 'Distribute calculation tasks among consumer instances'

    def handle(self, *args, **kwargs):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='calculation_queue')
        consumer_count =self.get_consumer_count()

        for i in range(consumer_count):
            message = {'operation': 'distribute', 'consumer_id': i}
            channel.basic_publish(exchange='', routing_key='calculation_queue', body=json.dumps(message))

        connection.close()

    def get_consumer_count(self):
        consumer_count_str = os.getenv('CONSUMER_COUNT')
        if consumer_count_str:
            try:
                consumer_count = int(consumer_count_str)
                return consumer_count
            except ValueError:
                
                return 3  # Default to a fixed number if value is invalid
        else:
            return 3
