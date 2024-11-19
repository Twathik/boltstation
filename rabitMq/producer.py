from connection import getConnection, routing_key
from queue_names import get_user_info


connection = getConnection()

channel = connection.channel()

channel.queue_declare(queue=get_user_info)

message = "405a44d3-3a76-47a9-a741-5c30aa2b21e0"

channel.basic_publish(exchange="", routing_key=get_user_info, body=message)

print(f"sent message {message}")

connection.close()
