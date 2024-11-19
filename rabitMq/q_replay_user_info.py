# -*- coding: utf-8 -*-
# pylint: disable=C0111,C0103,R0205

import asyncio
import functools
import logging
from typing import Optional
import pika.adapters.blocking_connection
import signal
import sys
import time
import pika

from pika.adapters.asyncio_connection import AsyncioConnection
from pika.exchange_type import ExchangeType
from llm_queue_utils.general_utils.ConsumerClass import Consumer, ReconnectingConsumer
from llm_queue_utils.get_user_info_q.generate_user_info_model import (
    generate_user_info_model,
    generate_user_info_error,
)
from queue_names import (
    REPLAY_USER_INFO_EXCHANGE,
    replay_user_info,
)
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


REPLAY_CONSUMER_EXCHANGE = REPLAY_USER_INFO_EXCHANGE
REPLAY_CONSUMER_EXCHANGE_TYPE = ExchangeType.fanout
REPLAY_CONSUMER_QUEUE = replay_user_info
REPLAY_CONSUMER_ROUTING_KEY = ""


async def on_info_parsed(
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
            if body.decode("utf-8") == "200":

                await generate_user_info_model(
                    scannedDocumentId=properties.correlation_id
                )

                ch.basic_ack(delivery_tag=method.delivery_tag)
                pass
            else:

                await generate_user_info_error(
                    scannedDocumentId=properties.correlation_id
                )
                pass
            acknowledged = True
            break
        except Exception as e:
            retry_count += 1
            print(f"error processing user infos {retry_count}/{max_retries}", e)
            if retry_count < max_retries:
                time.sleep(3)

    if not acknowledged:
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
        callbackFunction=on_info_parsed,
        EXCHANGE=REPLAY_USER_INFO_EXCHANGE,
        EXCHANGE_TYPE=REPLAY_CONSUMER_EXCHANGE_TYPE,
        LOGGER=LOGGER,
        loop=loop,
        QUEUE=REPLAY_CONSUMER_QUEUE,
        ROUTING_KEY=REPLAY_CONSUMER_ROUTING_KEY,
        durable=True,
    )
    print("start replaying messages")
    consumer.run()


if __name__ == "__main__":
    # Handle signals for graceful shutdown
    signal.signal(signal.SIGINT, shutdown_rabbitmq_consumer)
    signal.signal(signal.SIGTERM, shutdown_rabbitmq_consumer)

    try:
        main()
        print("second")

    except Exception as e:
        print(f"Error: {e}")
        shutdown_rabbitmq_consumer(None, None)
