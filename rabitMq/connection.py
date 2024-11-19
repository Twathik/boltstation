import pika


routing_key = "bolt-queue"


def getConnection():
    credentials = pika.PlainCredentials("rabbit", "rabbit")
    Connection_parameters = pika.ConnectionParameters(
        "100.108.14.46", credentials=credentials, virtual_host="bolt-vhost"
    )

    connection = pika.BlockingConnection(Connection_parameters)

    return connection
