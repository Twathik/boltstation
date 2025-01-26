import pika
from pika.exchange_type import ExchangeType
from src.lib.ai_document.utils.queue_names import PUBLISH_CHUNK_EXCHANGE


routing_key = "bolt-queue"


class RabbitMQManager:
    def __init__(self):
        self.connection = None
        self.channel = None

    def connect(self):
        """
        Establish a connection to RabbitMQ and create a channel.
        """
        if not self.connection or self.connection.is_closed:
            credentials = pika.PlainCredentials("rabbit", "rabbit")
            Connection_parameters = pika.ConnectionParameters(
                "100.108.14.46", credentials=credentials, virtual_host="bolt-vhost"
            )
            self.connection = pika.BlockingConnection(Connection_parameters)
            self.channel = self.connection.channel()

            print("RabbitMQ connection established.")

    def close(self):
        """
        Close the RabbitMQ connection.
        """
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            print("RabbitMQ connection closed.")

    def publish_message(self, exchange: str, routing_key: str, body: str, queue: str):
        """
        Publish a message to the RabbitMQ exchange.
        """

        if not self.channel or self.channel.is_closed:
            print("Channel is None or closed. Reconnecting...")
            self.connect()  # Reconnect if the channel is unavailable
        self.channel.exchange_declare(
            exchange=exchange, exchange_type=ExchangeType.direct, durable=False
        )
        self.channel.queue_declare(queue=queue, durable=False)
        self.channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=body,
        )
        print(f"Message published to {exchange}:{routing_key}")
