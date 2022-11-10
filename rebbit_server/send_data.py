import pika
import json
from loguru import logger


def send_data(data: list):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    # create queue
    channel.queue_declare(queue='steam')

    # can send only bite or string
    body = json.dumps(data)

    channel.basic_publish(exchange='', routing_key='hello', body=body)
    logger.info(f"Send {body}")
    connection.close()
