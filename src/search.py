from PIL import Image
from .embeded import image_embeding
from .database import get_connection

def search_similar_images(query_embedding, top_k=3):
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id,
                   embedding <=> %s::vector AS distance
            FROM image_embeddings
            ORDER BY embedding <=> %s::vector
            LIMIT %s
            """,
            (
                query_embedding.tolist(),
                query_embedding.tolist(),
                top_k
            )
        )

        results = cursor.fetchall()

    connection.close()

    return results


query_image = Image.open("/home/aggrey/img_search/testdata/0a48c9b477.jpg").convert("RGB")

query_embedding = image_embeding(query_image)

results = search_similar_images(query_embedding)

for result in results:
    print(result)