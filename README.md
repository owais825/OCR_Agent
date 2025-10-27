A **LangChain + LangSmith** powered OCR (Optical Character Recognition) pipeline that extracts text from images with full observability, tracing, and modular design.  

This project demonstrates how to **trace every step of an AI pipeline** — from image input to OCR text extraction — using **LangSmith’s observability tools**, ensuring transparency, debuggability, and reliability.  

---

## 🌟 Key Features  

- ✅ **AI-Powered OCR** — Converts images (JPG, PNG, JPEG) into text  
- ✅ **LangSmith Tracing** — Complete trace visibility for each pipeline step  
- ✅ **Streamlit Frontend** — Simple drag-and-drop UI  
- ✅ **Modular Design** — Clean separation between `app`, `main`, and `tools`  
- ✅ **Deprecation-Free** — Uses `use_container_width` for Streamlit image display  
- ✅ **Cloud-Ready** — Deployable on Streamlit Cloud or Hugging Face Spaces  

---

## 🏗️ Architecture Overview  

### 🔹 System Components  

| Component | Description |
|------------|-------------|
| `app.py` | Streamlit frontend for image upload and OCR display |
| `main.py` | Core pipeline orchestrator with LangSmith tracing |
| `agent/tools.py` | OCR extraction tool using Pillow and pytesseract |
| `.env` | LangSmith credentials and configuration |
| `uploads/` | Temporary folder for user-uploaded images |

---

### 🔹 Process Flow (ASCII Diagram)
    ┌──────────────┐
│  User Upload │
└──────┬───────┘
       │
       ▼
┌─────────────────┐
│   app.py (UI)   │
└────────┬────────┘
         │ calls
         ▼
┌───────────────────────────┐
│   main.py (Pipeline)      │
│   @traceable run_pipeline()│
└────────┬──────────────────┘
         │ calls
         ▼
┌────────────────────────────┐
│   agent/tools.py           │
│   @traceable extract_text()│
│   → Read image             │
│   → OCR text               │
│   → Return result          │
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────────┐
│   LangSmith Dashboard      │
│   Trace Visualization      │
└────────────────────────────┘



---

### 🔹 Mermaid Architecture Diagram  

```mermaid
flowchart TD
A[User Upload Image] --> B[app.py - Streamlit UI]
B --> C[main.py - run_pipeline()]
C --> D[agent/tools.py - extract_text()]
D --> E[LangSmith Dashboard - Traces, Metrics, Logs]
⚙️ Setup Instructions
1️⃣ Clone Repository
bash
Copy code
git clone https://github.com/yourusername/ocr-agent-langsmith.git
cd ocr-agent-langsmith
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # macOS/Linux
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
If you don’t have a requirements.txt file yet:

bash
Copy code
pip install streamlit langchain langsmith pillow pytesseract python-dotenv
4️⃣ Configure Environment Variables
Create a .env file in your root directory:

bash
Copy code
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="your_langsmith_api_key"
LANGCHAIN_PROJECT="OCR-Agent"
🔑 Get your API key from smith.langchain.com.

▶️ Run the Application
bash
Copy code
streamlit run app.py
Visit your local app:
👉 http://localhost:8501

📊 Trace Visualization in LangSmith
All function calls wrapped with @traceable are automatically logged in LangSmith.
You can view:

Inputs and outputs of each traced call

Timing and performance metrics

Nested trace hierarchy

Exceptions and stack traces

Example Trace Tree:
scss
Copy code
Streamlit User Session
│
└── run_pipeline()  → main.py
     │
     └── extract_text() → tools.py
🧠 Example Output
scss
Copy code
✅ Image uploaded successfully!
🔍 Extracting text... Please wait...

📝 Extracted Text:
"The quick brown fox jumps over the lazy dog"
💼 Technical Summary
Category	Description
Frameworks	LangChain, LangSmith, Streamlit
Language	Python 3.10+
Libraries	pytesseract, Pillow, dotenv
Tracing Tool	LangSmith Dashboard
Deployment	Streamlit Cloud / Hugging Face Spaces
Database	None (Traces stored remotely on LangSmith)

🧩 Future Enhancements
📄 PDF OCR & batch image extraction

🌐 Multi-language OCR (English, Hindi, Arabic, etc.)

🧠 LangGraph + LangServe integration

☁️ Cloud deployment with persistent logs

🔍 Enhanced error tracing with metadata

🧾 License
This project is licensed under the MIT License.
You’re free to use, modify, and distribute it with proper attribution.
