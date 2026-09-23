from pathlib import Path
from PIL import Image

from .embeded import image_embeding

from database import save_embedding
image_folder = Path("testdata")

for image_path in image_folder.iterdir():
    if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue

    image_id = image_path.stem

    image = Image.open(image_path).convert("RGB")

    embedding = image_embeding(image)

    save_embedding(image_id, embedding)

    print(image_id, embedding.shape)