import streamlit as st
import os
from langsmith import traceable
from main import run_pipeline

# Streamlit app setup
st.set_page_config(page_title="OCR Agent", layout="centered")
st.title("🧠 OCR Agent — Image Text Extractor")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Directory to store temp uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@traceable(name="streamlit_user_session")
def process_uploaded_image(uploaded_file_path: str):
    """Run the OCR pipeline on uploaded image."""
    return run_pipeline(uploaded_file_path)


if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    
    # Save uploaded image
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Image uploaded successfully!")

    # Process button
    if st.button("🔍 Extract Text"):
        with st.spinner("Extracting text... Please wait..."):
            result = process_uploaded_image(file_path)

            # Find the tool output message
            messages_list = result.get("messages", [])
            extracted_text = None
            for msg in messages_list:
                if (
                    msg.__class__.__name__ == "ToolMessage"
                    and hasattr(msg, "content")
                    and msg.content.strip()
                ):
                    extracted_text = msg.content.strip()
                    break

            if extracted_text:
                st.subheader("📝 Extracted Text")
                st.text_area("Text", extracted_text, height=300)
            else:
                st.warning("No text could be extracted from the image.")
