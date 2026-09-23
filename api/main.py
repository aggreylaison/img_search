from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

from src.embeded import image_embeding
from src.search import search_similar_images


app = FastAPI(
    title="Soko Plus Image Search API"
)


@app.get("/")
def home():
    return {
        "message": "Soko Plus Image Search API is running"
    }


@app.post("/search")
async def search_image(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image = Image.open(
        io.BytesIO(image_bytes)
    ).convert("RGB")

    query_embedding = image_embeding(image)

    results = search_similar_images(
        query_embedding,
        top_k=5
    )

    return {
        "results": [
            {
                "id": image_id,
                "distance": float(distance)
            }
            for image_id, distance in results
        ]
    }