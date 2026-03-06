import redis
import json



redis_client = redis.Redis.from_url("redis://localhost:6379/0")


def enqueue_product_operation(operation, data):
    message = {
        "operation": operation,
        "data": data
    }

    redis_client.lpush("product_queue", json.dumps(message))