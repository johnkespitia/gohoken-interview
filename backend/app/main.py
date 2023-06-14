from fastapi import FastAPI
from .cache import generate_image_cache
from fastapi.openapi.utils import get_openapi
from typing import List, Tuple

app = FastAPI()


@app.get("/images", tags=["Images"], response_model=List[Tuple[str, str]])
async def get_images():
    """
    Retrieve a list of images from a data cache getting those images from https://api.slingacademy.com/public/sample-photos/.

    Returns:
        List[Tuple[str, str]]: A list of image URLs and titles.
    """
    return generate_image_cache()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Image API",

        version="1.0.0",
        description="API to retrieve images from https://api.slingacademy.com/public/sample-photos/.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi