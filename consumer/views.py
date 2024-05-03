from django.shortcuts import render

# Create your views here.
import pika
from django.conf import settings
from django.http import HttpResponse

def receive_message(request):
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

    # Consume messages from the queue
    method_frame, header_frame, body = channel.basic_get(queue=settings.RABBITMQ_QUEUE_NAME)

    # Close connection
    connection.close()
    

    if method_frame:
        return HttpResponse(f"Received message from RabbitMQ queue: {body.decode()}")
    else:
        return HttpResponse("No messages in queue")