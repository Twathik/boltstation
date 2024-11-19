import time
from openai import max_retries
import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import BasicProperties
from connection import getConnection
from lib.redisClient import redis_client
from queue_names import OMNIPARSER_EXCHANGE, get_user_info, get_user_info_omniparser
import asyncio
from llm_queue_utils.get_user_info_q.generate_user_info_model import (
    generate_user_info_error,
    generate_user_info_model,
)
import signal
import sys


def get_user_info_queue() -> None:
    # Explicitly specify the type of the connection

    def on_info_parsed(
        ch: BlockingChannel,
        method: pika.spec.Basic.Deliver,
        properties: BasicProperties,
        body: bytes,
    ) -> None:
        max_retries = 5
        retry_count = 0
        while retry_count < max_retries:
            try:
                if body.decode("utf-8") == "200":

                    asyncio.run(
                        generate_user_info_model(
                            scannedDocumentId=properties.correlation_id
                        )
                    )
                    ch.basic_ack(delivery_tag=method.delivery_tag)
                    pass
                else:
                    asyncio.run(
                        generate_user_info_error(
                            scannedDocumentId=properties.correlation_id
                        )
                    )
                    ch.basic_ack(delivery_tag=method.delivery_tag)
                    pass
                pass
            except Exception as e:
                retry_count += 1
                print(f"error processing user infos {retry_count}/{max_retries}", e)
                if retry_count == max_retries:
                    print("maximum numbers of retries reached")
                    ch.basic_ack(delivery_tag=method.delivery_tag)
                else:
                    time.sleep(3)

    def on_root_message_received(
        ch: BlockingChannel,
        method: pika.spec.Basic.Deliver,
        properties: BasicProperties,
        body: bytes,
    ) -> None:
        cor_id = body.decode("utf-8")
        print(f"Sending Request: {cor_id}")

        ch.basic_publish(
            exchange=OMNIPARSER_EXCHANGE,
            routing_key=get_user_info_omniparser,
            properties=pika.BasicProperties(
                reply_to=reply_queue.method.queue,
                correlation_id=cor_id,
                expiration=str(60000),
            ),
            body=body,
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Declare the channel and specify its type
    channel: BlockingChannel = rabbitmq_connection.channel()

    channel.queue_declare(queue=get_user_info, durable=True)
    reply_queue = channel.queue_declare(queue="", exclusive=True)

    channel.basic_consume(
        queue=get_user_info, on_message_callback=on_root_message_received
    )

    channel.basic_consume(
        queue=reply_queue.method.queue,
        on_message_callback=on_info_parsed,
    )

    print("start consuming user info messages")
    # Start consuming messages
    channel.start_consuming()


def start_rabbitmq_consumer():
    global rabbitmq_connection
    rabbitmq_connection = getConnection()
    get_user_info_queue()


def shutdown_rabbitmq_consumer(signum, frame):
    print("Shutting down gracefully...")

    # Close Redis connection
    redis_client.close()
    print("Redis client closed.")

    # Close RabbitMQ connection
    if rabbitmq_connection and not rabbitmq_connection.is_closed:
        rabbitmq_connection.close()
        print("RabbitMQ connection closed.")

    sys.exit(0)


if __name__ == "__main__":
    # Handle signals for graceful shutdown
    signal.signal(signal.SIGINT, shutdown_rabbitmq_consumer)
    signal.signal(signal.SIGTERM, shutdown_rabbitmq_consumer)

    try:

        start_rabbitmq_consumer()

    except Exception as e:
        print(f"Error: {e}")
        shutdown_rabbitmq_consumer(None, None)
