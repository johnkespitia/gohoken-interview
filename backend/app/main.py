from fastapi import FastAPI
from .cache import generate_image_cache

app = FastAPI()


@app.get("/images")
async def get_images():
    return generate_image_cache()
