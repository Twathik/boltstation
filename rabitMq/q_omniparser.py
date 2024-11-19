# -*- coding: utf-8 -*-
# pylint: disable=C0111,C0103,R0205

import asyncio
import functools
import logging
import pika.adapters.blocking_connection
import signal
import sys
import time
import pika

from pika.adapters.asyncio_connection import AsyncioConnection
from pika.exchange_type import ExchangeType
from llm_queue_utils.general_utils.ConsumerClass import Consumer, ReconnectingConsumer
from llm_queue_utils.get_user_info_q.omniparse import parse
from queue_names import OMNIPARSER_EXCHANGE, get_user_info_omniparser
from lib.redisClient import redis_client
from dotenv import load_dotenv
import os

load_dotenv()

AMQP_URL = os.getenv("AMQP_URL", "amqp://rabbit:rabbit@100.108.14.46:5672/bolt-vhost")

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

EXCHANGE = OMNIPARSER_EXCHANGE
EXCHANGE_TYPE = ExchangeType.fanout
QUEUE = get_user_info_omniparser
ROUTING_KEY = ""


async def on_message_received(
    ch: AsyncioConnection.channel,
    method: pika.spec.Basic.Deliver,
    properties: pika.BasicProperties,
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
            break
        except Exception as e:
            retry_count += 1
            print(f"error processing image {retry_count}/{max_retries}", e)
            if retry_count < max_retries:
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


def shutdown_rabbitmq_consumer(signum, frame):
    print("Shutting down gracefully...")

    # Close Redis connection
    redis_client.close()
    print("Redis client closed.")

    # Close rabbitmq_connection connection

    sys.exit(0)


def main():
    logging.basicConfig(level=logging.ERROR, format=LOG_FORMAT)

    consumer = ReconnectingConsumer(
        amqp_url=AMQP_URL,
        callbackFunction=on_message_received,
        EXCHANGE=EXCHANGE,
        EXCHANGE_TYPE=EXCHANGE_TYPE,
        LOGGER=LOGGER,
        loop=loop,
        QUEUE=QUEUE,
        ROUTING_KEY=ROUTING_KEY,
    )
    print("start parssing")
    consumer.run()


if __name__ == "__main__":
    # Handle signals for graceful shutdown
    signal.signal(signal.SIGINT, shutdown_rabbitmq_consumer)
    signal.signal(signal.SIGTERM, shutdown_rabbitmq_consumer)

    try:
        main()

    except Exception as e:
        print(f"Error: {e}")
        shutdown_rabbitmq_consumer(None, None)
