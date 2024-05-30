import pika,logging
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
        logger.info("Sent %r", message)

        connection.close()
   