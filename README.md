# LangChain + LangSmith OCR Pipeline

A **LangChain + LangSmith powered OCR (Optical Character Recognition) pipeline** that extracts text from images with full observability, tracing, and modular design. This project demonstrates how to trace every step of an AI pipeline — from image input to OCR text extraction — using LangSmith’s observability tools, ensuring transparency, debuggability, and reliability.

---

## 🌟 Key Features
- ✅ **AI-Powered OCR** — Converts images (JPG, PNG, JPEG) into text  
- ✅ **LangSmith Tracing** — Complete trace visibility for each pipeline step  
- ✅ **Streamlit Frontend** — Simple drag-and-drop UI  
- ✅ **Modular Design** — Clean separation between app, main, and tools  
- ✅ **Deprecation-Free** — Uses `use_container_width` for Streamlit image display  
- ✅ **Cloud-Ready** — Deployable on Streamlit Cloud or Hugging Face Spaces  

---

## 🏗️ Architecture Overview

### 🔹 System Components

| Component        | Description                                      |
|-----------------|--------------------------------------------------|
| `app.py`        | Streamlit frontend for image upload and OCR display |
| `main.py`       | Core pipeline orchestrator with LangSmith tracing |
| `agent/tools.py`| OCR extraction tool using Pillow and pytesseract |
| `.env`          | LangSmith credentials and configuration         |
| `uploads/`      | Temporary folder for user-uploaded images       |

### 🔹 Process Flow
User Upload Image
│
▼
app.py (UI)
│
▼
main.py (Pipeline)
│
▼
agent/tools.py (OCR extraction)
│
▼
LangSmith Dashboard (Traces, Metrics, Logs)
