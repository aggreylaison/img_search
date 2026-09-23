import streamlit as st
from PIL import Image

from src.embeded import image_embeding
from src.search import search_similar_images


st.set_page_config(
    page_title="Soko Plus Image Search",
    page_icon="🔎",
    layout="wide"
)


st.title("🔎 Soko Plus Image Search")
st.write("Upload a product image to find similar products.")


uploaded_file = st.file_uploader(
    "Upload a product image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Uploaded Image")
    st.image(image, width=300)

    if st.button("Search Similar Products"):

        with st.spinner("Searching..."):

            # Generate embedding for uploaded image
            query_embedding = image_embeding(image)

            # Search database
            results = search_similar_images(
                query_embedding,
                top_k=5
            )

        st.subheader("Similar Products")

        for image_id, distance in results:

            image_path = f"testdata/{image_id}.jpg"

            st.image(
                image_path,
                width=250,
                caption=f"ID: {image_id} | Distance: {distance:.4f}"
            )

else:

    st.info("Upload an image to start searching.")
