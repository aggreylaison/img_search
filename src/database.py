import psycopg


def get_connection():
    return psycopg.connect(
        dbname="sokoplus_ai",
        user="aggrey"
    )


def save_embedding(image_id, embedding):
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO image_embeddings (id, embedding)
            VALUES (%s, %s)
            """,
            (image_id, embedding.tolist())
        )

    connection.commit()
    connection.close()