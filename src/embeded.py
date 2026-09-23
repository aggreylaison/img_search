from .load import processor,model 
import torch
import numpy as np
def image_embeding(image):
    input=processor(images=image, return_tensors="pt")
    with torch.no_grad():
        output=model.get_image_features(**input)

    embeddings=output.pooler_output.squeeze().numpy()

    return embeddings

