from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import pika
import json

def add(request):
    # Get operands from request
    operand1 = request.GET.get('operand1')
    operand2 = request.GET.get('operand2')

    # Publish calculation request to RabbitMQ
    message = {'operation': 'add', 'operand1': operand1, 'operand2': operand2}
    publish_message(message)

    return JsonResponse({'message': 'Calculation request sent successfully'})

def publish_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='calculation_queue')
    channel.basic_publish(exchange='', routing_key='calculation_queue', body=json.dumps(message))
    connection.close()

