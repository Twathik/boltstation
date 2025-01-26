# -*- coding: utf-8 -*-
# pylint: disable=C0111,C0103,R0205

import asyncio
import json
import logging
import time
import pika.adapters.blocking_connection
import signal
import sys
import pika

from pika.adapters.asyncio_connection import AsyncioConnection
from pika.exchange_type import ExchangeType
from pprintpp import pprint
from llm_queue_utils.general_utils.ConsumerClass import ReconnectingConsumer
from llm_queue_utils.publish_chunck_utils.generate_ai_content import generate_ai
from llm_queue_utils.summarize_document.summarize_medicalDocument import (
    summarize_medicalDocument,
)
from queue_names import (
    publish_chunk,
    PUBLISH_CHUNK_EXCHANGE,
    summarize_document,
    SUMMARIZE_DOCUMENT_EXCHANGE,
)
from lib.redisClient import redis_client
from dotenv import load_dotenv
import os
from langchain_ollama import OllamaLLM

load_dotenv()

AMQP_URL = os.getenv("AMQP_URL", "amqp://rabbit:rabbit@100.108.14.46:5672/bolt-vhost")

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

llm = OllamaLLM(
    model="gemma2:latest",
    # model="phi4:latest",
    temperature=0.2,
    # other params...
)


async def on_root_message_received(
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
            payload = json.loads(body.decode("utf-8"))
            start_time = time.time()
            await generate_ai(
                chunk=payload["chunk"],
                temporaryChanelId=payload["temporaryChanelId"],
                llm=llm,
                content=payload["content"],
                sex=payload["sex"],
                target_message_Id=payload["target_message_Id"],
            )
            end_time = time.time()
            exec_time = end_time - start_time
            print("execussion time", exec_time)
            # await summarize_medicalDocument(document_id=body.decode("utf-8"))
            ch.basic_ack(delivery_tag=method.delivery_tag)
            print(payload["target_message_Id"])
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
        callbackFunction=on_root_message_received,
        EXCHANGE=PUBLISH_CHUNK_EXCHANGE,
        EXCHANGE_TYPE=ExchangeType.direct,
        LOGGER=LOGGER,
        loop=loop,
        QUEUE=publish_chunk,
        ROUTING_KEY="chunk",
        durable=False,
    )
    print("start recieving messages")
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
