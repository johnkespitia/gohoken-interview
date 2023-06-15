import redis
import os

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_db = os.getenv("REDIS_DB")
redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

def store_image_cache(url, title):
    redis_client.set(url, title)

def get_all_images():
    image_keys = redis_client.keys('*')

    image_data = []
    for key in image_keys:
        url = key.decode()
        title = redis_client.get(url).decode()
        image_data.append((url, title))

    return image_data