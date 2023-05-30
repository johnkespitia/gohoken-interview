import requests


def generate_image_cache():
    """
    Generate a list of images to cache from
    https://api.slingacademy.com/v1/sample-data/photos?offset=5&limit=20
    """
    res = requests.get(
        "https://api.slingacademy.com/v1/sample-data/photos?offset=5&limit=20"
    )
    return process_image_cache(res)


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
    image_urls = []
    data = response.json()

    for image in data["photos"]:
        image_urls.append(image["url"])

    # duplicate randomly 30% of images to simulate a larger cache
    # DO NOT REMOVE THIS IS PART OF THE FRONTEND TEST
    image_urls.extend(image_urls[: len(image_urls) // 3])

    # add a few more images that will fail to load
    # DO NOT REMOVE THIS IS PART OF THE FRONTEND TEST
    image_urls.extend(
        [
            "https://api.slingacademy.com/public/sample-photos/asd.jpeg",
            "https://api.slingacademy.com/public/sample-photos/dsa.jpeg",
            "https://api.slingacademy.com/public/sample-photos/sad.jpeg",
        ]
    )

    return image_urls
