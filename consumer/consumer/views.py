from django.shortcuts import render
import pika

def display_result(request):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='results')
    method_frame, header_frame, body = channel.basic_get(queue='results')
    if method_frame:
        result = body.decode('utf-8')
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        connection.close()
        return render(request, 'result.html', {'result': result})
    connection.close()
    return render(request, 'result.html', {'result': 'No results available'})