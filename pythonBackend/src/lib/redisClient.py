from redis import Redis
import os

redis_host = os.getenv("HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

redis_client = Redis(
    host=redis_host,
    port=redis_port,
    db=0,
    decode_responses=True,
    password=os.getenv("REDIS_PSW"),
)

notification_chanel = "boltNotifications"
