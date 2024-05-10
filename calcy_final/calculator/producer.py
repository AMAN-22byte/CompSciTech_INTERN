import pika,logging
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

def send_message(message):
    
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=settings.RABBITMQ_HOST,
                port=settings.RABBITMQ_PORT,
                credentials=pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASS)
            )
        )
        channel = connection.channel()
        channel.queue_declare(queue='operands')

        channel.basic_publish(exchange='', routing_key='operands', body=message)
        print(" [x] Sent %r" % message)
        # logger.info("Sent message: %r", message)

        connection.close()
   