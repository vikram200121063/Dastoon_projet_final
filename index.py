import streamlit as st
import requests
from PIL import Image
import io

# API Configuration
API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "image/png",
    "Authorization": "Bearer VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM",
    "Content-Type": "application/json",
}

# Function to query the API and get image bytes
def query_api(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit App
def main():
    st.title("Comic Strip Generator")

    # Form to input text for 10 comic panels
    comic_texts = []
    for i in range(10):
        comic_texts.append(st.text_area(f"Panel {i + 1} Text", key=f"panel_{i}"))

    # Button to generate comic strip
    if st.button("Generate Comic Strip"):
        # Generate comic strip using the API
        generated_images = []
        for text in comic_texts:
            image_bytes = query_api({"inputs": text})
            image = Image.open(io.BytesIO(image_bytes))
            generated_images.append(image)

        # Display the generated comic strip
        for i, image in enumerate(generated_images):
            st.image(image, caption=f"Panel {i + 1}", use_column_width=True)

if _name_ == "_main_":
    main()