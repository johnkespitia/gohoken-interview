import requests
from cachetools import TTLCache


session = requests.Session()
session.headers['Connection'] = 'keep-alive'
cache = TTLCache(maxsize=1000, ttl=3600)
def generate_image_cache():
    """
    Generate a list of images to cache from
    https://api.slingacademy.com/v1/sample-data/photos?offset=5&limit=20
    """
    offset = 0
    if "image_data" in cache:
        offset = len(cache["image_data"])
    else:
        cache["image_data"] = []
    headers = {'Accept-Encoding': 'gzip'}
    res = session.get(f"https://api.slingacademy.com/v1/sample-data/photos?offset={offset}&limit=20", headers=headers)
    image_data = process_image_cache(res)
    print(image_data)
    cache["image_data"].extend(image_data)
    print(cache["image_data"])
    return cache['image_data']


def process_image_cache(response: requests.Response):
    """
    Process the image cache and return a list of image URLs

    expected response
    {
        "photos": [
                {
            "description": "...",
            "url": "https://api.slingacademy.com/public/sample-photos/25.jpeg",
            "title": "Certainly than need enjoy understand right",
            "user": 15,
            "id": 25
            }
        }
    }

    """
    image_data = []
    if response.status_code == 200:
        data = response.json()
        photos = data.get("photos", [])
        for image in photos:
            url = image.get("url")
            title = image.get("title")
            if url and title:
                image_data.append((url, title))

        # duplicate randomly 30% of images to simulate a larger cache
        # DO NOT REMOVE THIS IS PART OF THE FRONTEND TEST
        image_data.extend(image_data[:len(image_data) // 3])

        # add a few more images that will fail to load
        # DO NOT REMOVE THIS IS PART OF THE FRONTEND TEST
        failed_data = [
            ("https://api.slingacademy.com/public/sample-photos/asd.jpeg", "Failed Image 1"),
            ("https://api.slingacademy.com/public/sample-photos/dsa.jpeg", "Failed Image 2"),
            ("https://api.slingacademy.com/public/sample-photos/sad.jpeg", "Failed Image 3"),
        ]
        image_data.extend(failed_data)

    return image_data
