import base64
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langsmith import traceable
from dotenv import load_dotenv

load_dotenv()

# Initialize vision-capable LLM
vision_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


@traceable(name="load_image")
def load_image(img_path: str) -> bytes:
    """Reads an image file as bytes."""
    with open(img_path, "rb") as image_file:
        return image_file.read()


@traceable(name="encode_image")
def encode_image(image_bytes: bytes) -> str:
    """Encodes image bytes into Base64 string for model input."""
    return base64.b64encode(image_bytes).decode("utf-8")


@traceable(name="extract_with_model")
def extract_with_model(image_base64: str) -> str:
    """Sends Base64 image to Gemini Vision model for text extraction."""
    message = [
        HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": (
                        "Extract all the text from this image. "
                        "Return only the extracted text, no explanations."
                    ),
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{image_base64}"},
                },
            ]
        )
    ]
    response = vision_llm.invoke(message)
    return response.content.strip()


@traceable(name="extract_text_pipeline")
def _extract_text_pipeline(img_path: str) -> str:
    """
    Internal pipeline that chains image loading, encoding,
    and extraction — fully traceable in LangSmith.
    """
    image_bytes = load_image(img_path)
    image_base64 = encode_image(image_bytes)
    extracted_text = extract_with_model(image_base64)
    return extracted_text


@tool
def extract_text(img_path: str) -> str:
    """
    Public tool wrapper for LangGraph.
    Extracts text from an image by calling the internal traced pipeline.
    """
    try:
        return _extract_text_pipeline(img_path)
    except Exception as e:
        error_msg = f"Error extracting text: {str(e)}"
        print(error_msg)
        return ""
