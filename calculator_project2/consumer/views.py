from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import pika
import json

def consume_message(request):
    # Consume calculation request from RabbitMQ
    result = consume_calculation()

    return JsonResponse(result)

def consume_calculation():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='calculation_queue')
    method_frame, header_frame, body = channel.basic_get(queue='calculation_queue', auto_ack=True)
    connection.close()

    if body:
        message = json.loads(body.decode('utf-8'))
        operation = message.get('operation')
        operand1 = float(message.get('operand1'))
        operand2 = float(message.get('operand2'))
        result = perform_operation(operation, operand1, operand2)
        return {'result': result}
    else:
        return {'error': 'No calculation request found'}

def perform_operation(operation, operand1, operand2):
    if operation == 'add':
        return operand1 + operand2
    elif operation == 'subtract':
        return operand1 - operand2
    elif operation == 'multiply':
        return operand1 * operand2
    elif operation == 'divide':
        if operand2 != 0:
            return operand1 / operand2
        else:
            return 'Division by zero error'
    else:
        return 'Invalid operation'
