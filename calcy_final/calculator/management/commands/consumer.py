import pika,os,logging
from django.core.management.base import BaseCommand
from django.conf import settings


# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('application.log')
handler.setLevel(logging.INFO)
handler.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(handler)

calculation_result=None

def calculate_callback(ch, method, properties, body):
    global calculation_result
    operands = body.decode().split(',')
    operator = operands[0]
    num1 = float(operands[1])
    num2 = float(operands[2])

    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    logger.info("Received %r", body)
    logger.info("Result: %r", result)

    print(" [x] Received %r" % body)
    print(" [x] Result: %r" % result)

    # Send result back to user 
    calculation_result=result

def consume_messages():

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calcy_final.settings')
    import django
    django.setup()
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASS)
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue='operands')

    channel.basic_consume(queue='operands', on_message_callback=calculate_callback, auto_ack=True)

    logger.info('Waiting for messages. To exit press CTRL+C')

    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    try:
        channel.start_consuming()
    except Exception as e:
        print('not consuming')
        connection.close()
    # consume_messages()


# if __name__ == '__main__':
#     consume_messages()

class Command(BaseCommand):
    help = 'Consume messages from RabbitMQ'

    def handle(self, *args, **kwargs):
        consume_messages()