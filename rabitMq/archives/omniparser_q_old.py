import signal
import sys
from openai import max_retries
import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import BasicProperties
from connection import getConnection
from queue_names import get_user_info_omniparser
from llm_queue_utils.get_user_info_q.omniparse import (
    parse,
)
import asyncio
import time
from lib.redisClient import redis_client
from concurrent.futures import ThreadPoolExecutor

loop = asyncio.get_event_loop()


async def on_message_received(
    ch: BlockingChannel,
    method: pika.spec.Basic.Deliver,
    properties: BasicProperties,
    body: bytes,
) -> None:
    max_retries = 3
    retry_count = 0
    acknowledged = False
    while retry_count < max_retries:
        try:
            message = await parse(patientIdentityScanId=body.decode("utf-8"))
            ch.basic_publish(
                "",
                routing_key=properties.reply_to,
                body=message,
                properties=pika.BasicProperties(
                    correlation_id=properties.correlation_id
                ),
            )
            ch.basic_ack(delivery_tag=method.delivery_tag)
            acknowledged = True
            pass
        except Exception as e:
            retry_count += 1
            print(f"error processing image {retry_count}/{max_retries}", e)
            if retry_count == max_retries:
                print("maximum numbers of retries reached")
                ch.basic_publish(
                    "",
                    routing_key=properties.reply_to,
                    body="500",
                    properties=pika.BasicProperties(
                        correlation_id=properties.correlation_id
                    ),
                )
                ch.basic_ack(delivery_tag=method.delivery_tag)
            else:
                time.sleep(3)
        # Handle failure after retries
    if not acknowledged:
        print("Maximum retries reached, sending error response.")
        ch.basic_publish(
            exchange="",
            routing_key=properties.reply_to,
            body="500",
            properties=pika.BasicProperties(correlation_id=properties.correlation_id),
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)


def on_message_received_sync_wrapper(ch, method, properties, body):
    # Schedule the async function in the asyncio loop
    asyncio.run_coroutine_threadsafe(
        on_message_received(ch, method, properties, body), loop
    )


def get_user_info_omniparser_q() -> None:
    # Explicitly specify the type of the connection

    # Declare the channel and specify its type
    channel: BlockingChannel = rabbitmq_connection.channel()

    channel.queue_declare(queue=get_user_info_omniparser)

    channel.basic_consume(
        queue=get_user_info_omniparser,
        on_message_callback=on_message_received_sync_wrapper,
    )

    print("start consuming user info omniparser messages")
    # Start consuming messages
    channel.start_consuming()


def start_rabbitmq_consumer():
    global rabbitmq_connection
    rabbitmq_connection = getConnection()
    get_user_info_omniparser_q()


def shutdown_rabbitmq_consumer(signum, frame):
    print("Shutting down gracefully...")

    # Close Redis connection
    redis_client.close()
    print("Redis client closed.")

    # Close rabbitmq_connection connection
    if rabbitmq_connection and not rabbitmq_connection.is_closed:
        rabbitmq_connection.close()
        print("rabbitmq_connection connection closed.")

    sys.exit(0)


if __name__ == "__main__":
    # Handle signals for graceful shutdown
    signal.signal(signal.SIGINT, shutdown_rabbitmq_consumer)
    signal.signal(signal.SIGTERM, shutdown_rabbitmq_consumer)

    try:
        executor = ThreadPoolExecutor(1)
        executor.submit(start_rabbitmq_consumer)
        loop.run_forever()

    except Exception as e:
        print(f"Error: {e}")
        loop.stop()
        executor.shutdown()
        shutdown_rabbitmq_consumer(None, None)
