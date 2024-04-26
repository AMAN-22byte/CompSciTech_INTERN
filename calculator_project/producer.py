import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='calculation_tasks')

def send_calculation_task(task):
    channel.basic_publish(exchange='', routing_key='calculation_tasks', body=task)
    print(" [x] Sent %r" % task)

connection.close()
