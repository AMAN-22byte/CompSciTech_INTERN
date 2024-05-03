from django.shortcuts import render
from.models import Calculation
import pika

def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        calculation = Calculation(expression=expression)
        calculation.save()
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='calculations')
        channel.basic_publish(exchange='', routing_key='calculations', body=expression)
        connection.close()
        return render(request, 'calculator.html', {'message': 'Calculation submitted successfully'})
    return render(request, 'calculator.html')