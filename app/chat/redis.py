import os
import redis

redis_client = redis.Redis.from_url(url=os.getenv("REDIS_URI"), decode_responses=True)
