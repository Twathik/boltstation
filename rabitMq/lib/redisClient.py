import redis
from dotenv import load_dotenv
import os

load_dotenv()


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    password=os.getenv("REDIS_PSW", "123456789"),
    decode_responses=True,  # To handle string responses
)

notification_chanel = "boltNotifications"
