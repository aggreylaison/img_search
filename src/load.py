from transformers import AutoModel,AutoProcessor
import torch

model_name="google/siglip2-base-patch16-224"

processor=AutoProcessor.from_pretrained(model_name)
model=AutoModel.from_pretrained(model_name)

print("Model loaded successfully")

model.eval()