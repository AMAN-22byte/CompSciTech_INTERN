from django.shortcuts import render

# Create your views here.
import pika
from django.conf import settings
from django.http import HttpResponse

def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        # Connect to RabbitMQ server
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=settings.RABBITMQ_HOST,
                port=settings.RABBITMQ_PORT,
                credentials=pika.PlainCredentials(
                    username=settings.RABBITMQ_USERNAME,
                    password=settings.RABBITMQ_PASSWORD
                )
            )
        )
        channel = connection.channel()

        # Declare a queue
        channel.queue_declare(queue=settings.RABBITMQ_QUEUE_NAME)

        # Publish message to the queue
        channel.basic_publish(
            exchange='',
            routing_key=settings.RABBITMQ_QUEUE_NAME,
            body=message
        )

        # Close connection
        connection.close()

        return HttpResponse("Message sent to RabbitMQ queue")
    else:
        return HttpResponse("Send Message Form")