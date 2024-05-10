import pika,os,logging
from django.conf import settings

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )

# logger = logging.getLogger(__name__)
# logger.debug('Debug message')
# logger.info('Info message')
# logger.warning('Warning message')
# logger.error('Error message')
# logger.critical('Critical message')

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

    print(" [x] Received %r" % body)
    print(" [x] Result: %r" % result)

    # logger.info("Received message: %r", body)
    # logger.info("Calculated result: %r", result)

    # Send result back to user 
    calculation_result=result

def consume_messages():

    # logger.info('Consumer started')

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


    # logger.info('Waiting for messages. To exit press CTRL+C')

    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    try:
        channel.start_consuming()
    except Exception as e:
        # logger.error('Error consuming messages: %s', str(e))
        print('not consuming')
        connection.close()
consume_messages()

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     consume_messages()